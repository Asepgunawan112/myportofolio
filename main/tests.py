from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

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
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_experience_page_has_edit_and_delete_buttons(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        edit_url = reverse("main:edit_experience_data", args=[self.experience.id])
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        self.assertContains(response, f'href="{edit_url}"')
        self.assertContains(response, f'action="{delete_url}"')
        self.assertContains(response, f'delete-experience-{self.experience.id}')

    def test_edit_experience_page_accessible(self):
        response = self.client.get(reverse("main:edit_experience_data", args=[self.experience.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/edit_experience.html")
        self.assertContains(response, self.experience.title)

    def test_delete_experience(self):
        response = self.client.post(reverse("main:delete_experience", args=[self.experience.id]))

        self.assertRedirects(response, reverse("main:show_experience"))
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())


    def test_certificate_page_accessible(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certificate.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_certificate_data_displayed_when_data_added(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertContains(response, self.certificate.title)
        self.assertContains(response, self.certificate.organization)
        self.assertContains(response, self.certificate.thumbnail)

    def test_empty_certificate_page(self):
        Certificate.objects.all().delete()
        response = self.client.get(reverse("main:show_certificate"))

        self.assertContains(response, "there are no certificates to display.")

    def test_certificate_page_has_edit_button(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertEqual(response.status_code, 200)
        edit_url = reverse("main:edit_certificate_data", args=[self.certificate.id])
        self.assertContains(response, f'href="{edit_url}"')

    def test_edit_certificate_page_accessible_and_contains_delete_modal(self):
        response = self.client.get(reverse("main:edit_certificate_data", args=[self.certificate.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/edit_certificate.html")
        self.assertContains(response, self.certificate.title)
        delete_url = reverse("main:delete_certificate", args=[self.certificate.id])
        self.assertContains(response, f'action="{delete_url}"')
        self.assertContains(response, f'delete-certificate-{self.certificate.id}')

    def test_delete_certificate(self):
        response = self.client.post(reverse("main:delete_certificate", args=[self.certificate.id]))

        self.assertRedirects(response, reverse("main:show_certificate"))
        self.assertFalse(Certificate.objects.filter(id=self.certificate.id).exists())