from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from main.models import Experience, Certificate


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.certificate = Certificate.objects.create(
            title="Sertifikat React",
            organization="WPU Course",
            date="2026-06-20",
            thumbnail="React_sertif.png",
        )
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        data = self.client.get(reverse("main:get_experience_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)
        self.assertEqual(data[0]["fields"]["description"], self.experience.description)
        self.assertEqual(data[0]["fields"]["category"], "part-time")
        self.assertIsNone(data[0]["fields"]["ended_at"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")
        self.assertEqual(self.client.get(reverse("main:get_experience_json")).json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        data = self.client.get(reverse("main:get_experience_json")).json()
        self.assertIsNotNone(data[0]["fields"]["ended_at"])

    def test_experience_page_has_edit_and_delete_buttons(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        placeholder_id = "00000000-0000-0000-0000-000000000000"
        self.assertContains(
            response,
            reverse("main:edit_experience_data", args=[placeholder_id]),
        )
        self.assertContains(
            response,
            reverse("main:delete_experience", args=[placeholder_id]),
        )

    def test_edit_experience_page_accessible(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse("main:edit_experience_data", args=[self.experience.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/edit_experience.html")
        self.assertContains(response, self.experience.title)

    def test_delete_experience(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse("main:delete_experience", args=[self.experience.id]))

        self.assertRedirects(response, reverse("main:show_experience"))
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())


    def test_certificate_page_accessible(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certificate.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_certificate_json_returns_all_data(self):
        second_certificate = Certificate.objects.create(
            title="Sertifikat Django",
            organization="Django Course",
            date="2026-07-20",
        )

        response = self.client.get(reverse("main:get_certificate_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            {item["pk"] for item in response.json()},
            {str(self.certificate.id), str(second_certificate.id)},
        )
        certificate_data = next(
            item for item in response.json() if item["pk"] == str(self.certificate.id)
        )
        self.assertEqual(certificate_data["fields"]["date"], "2026-06-20")

    def test_certificate_json_search_filters_by_title(self):
        Certificate.objects.create(
            title="Sertifikat Django",
            organization="Django Course",
            date="2026-07-20",
        )

        response = self.client.get(
            reverse("main:get_certificate_json"),
            {"title": "react"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["fields"]["title"], self.certificate.title)

    def test_certificate_data_displayed_when_data_added(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertEqual(response.status_code, 200)
        data = self.client.get(reverse("main:get_certificate_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.certificate.title)
        self.assertEqual(data[0]["fields"]["organization"], self.certificate.organization)
        self.assertEqual(data[0]["fields"]["thumbnail"], self.certificate.thumbnail)

    def test_empty_certificate_page(self):
        Certificate.objects.all().delete()
        response = self.client.get(reverse("main:show_certificate"))

        self.assertContains(response, "Belum ada sertifikat yang ditambahkan atau ditemukan.")
        self.assertEqual(self.client.get(reverse("main:get_certificate_json")).json(), [])

    def test_certificate_page_has_edit_button(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertEqual(response.status_code, 200)
        placeholder_id = "00000000-0000-0000-0000-000000000000"
        self.assertContains(
            response,
            reverse("main:edit_certificate_data", args=[placeholder_id]),
        )

    def test_edit_certificate_page_accessible_and_contains_delete_modal(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse("main:edit_certificate_data", args=[self.certificate.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/edit_certificate.html")
        self.assertContains(response, self.certificate.title)
        delete_url = reverse("main:delete_certificate", args=[self.certificate.id])
        self.assertContains(response, f'action="{delete_url}"')
        self.assertContains(response, f'delete-certificate-{self.certificate.id}')

    def test_delete_certificate(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse("main:delete_certificate", args=[self.certificate.id]))

        self.assertRedirects(response, reverse("main:show_certificate"))
        self.assertFalse(Certificate.objects.filter(id=self.certificate.id).exists())