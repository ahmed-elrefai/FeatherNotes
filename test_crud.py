import pytest
from django.test import TestCase, Client
from backend.main.models import Note

@pytest.mark.django_db
class TestCRUDOperations:
    def test_create_note(self):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        assert note.id is not None

    def test_read_note(self):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        # Read the note
        read_note = Note.objects.get(id=note.id)
        assert read_note.title == "Test Note"
        assert read_note.content == "This is a test note"

    def test_update_note(self):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        # Update the note
        note.title = "Updated Test Note"
        note.content = "This is an updated test note"
        note.save()
        # Read the updated note
        updated_note = Note.objects.get(id=note.id)
        assert updated_note.title == "Updated Test Note"
        assert updated_note.content == "This is an updated test note"

    def test_delete_note(self):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        # Delete the note
        note.delete()
        # Try to read the deleted note
        with pytest.raises(Note.DoesNotExist):
            Note.objects.get(id=note.id)

    def test_create_note_through_view(self, client):
        # Create a new note through the view
        response = client.post('/notes/', {'title': 'Test Note', 'content': 'This is a test note'})
        assert response.status_code == 201
        # Read the created note
        note = Note.objects.get(title='Test Note')
        assert note.title == 'Test Note'
        assert note.content == 'This is a test note'

    def test_read_note_through_view(self, client):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        # Read the note through the view
        response = client.get(f'/notes/{note.id}/')
        assert response.status_code == 200
        assert response.json()['title'] == 'Test Note'
        assert response.json()['content'] == 'This is a test note'

    def test_update_note_through_view(self, client):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        # Update the note through the view
        response = client.put(f'/notes/{note.id}/', {'title': 'Updated Test Note', 'content': 'This is an updated test note'})
        assert response.status_code == 200
        # Read the updated note
        updated_note = Note.objects.get(id=note.id)
        assert updated_note.title == 'Updated Test Note'
        assert updated_note.content == 'This is an updated test note'

    def test_delete_note_through_view(self, client):
        # Create a new note
        note = Note(title="Test Note", content="This is a test note")
        note.save()
        # Delete the note through the view
        response = client.delete(f'/notes/{note.id}/')
        assert response.status_code == 204
        # Try to read the deleted note
        with pytest.raises(Note.DoesNotExist):
            Note.objects.get(id=note.id)