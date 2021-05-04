from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from api.models import Song
from api.serializers import SongSerializer, PodcastSerializer, AudiobookSerializer


class AudioCreateTestCase(APITestCase):
    create_url = reverse('create')

    def test_song_create_audioFileType_missing(self):
        data = {
            "audioFileMetadata": {
                "name": "song",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_song_create_audioFileMetadata_missing(self):
        data = {
            "audioFileType": "song"
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_song_create_ideal(self):
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_song_create_name_missing(self):
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_song_create_duration_missing(self):
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_create_ideal(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_podcast_create_name_missing(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_create_duration_missing(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_create_host_missing(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 600,
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_create_participants_missing(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 600,
                "host": "host 1",
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_podcast_create_participants_greater_10(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5,"
                                "person6, person7, person8, person9, person10, person11"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_create_participants_name_greater_than_100_char(self):
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast",
                "duration": 600,
                "host": "host 1",
                "participants": "qwertyuiopasdfghjklzxcvbnmmnbvcxzasdfghjkkkkkklpo"
                                "iuytrewqazxswedcvfrtgbnhyujmkilpoiuyt"
                                "qwertyuiopasdfghjklzxcvbnmmnbvcxzasdfghjkkkkkklpo"
                                "iuytrewqazxswedcvfrtgbnhyujmkilpoiuyt,"
                                "person2, person3, person4, person5,"
                                "person6, person7, person8, person9, person10"
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_create_ideal(self):
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook",
                "author": "author 1",
                "narrator": "narrator 1",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_audiobook_create_name_missing(self):
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "author": "author 1",
                "narrator": "narrator 1",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_create_author_missing(self):
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook",
                "narrator": "narrator 1",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_create_narrator_missing(self):
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook",
                "author": "author 1",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_create_duration_missing(self):
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook",
                "author": "author 1",
                "narrator": "narrator 1",
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audioFileType_wrong_type(self):
        data = {
            "audioFileType": "wrong_type",
            "audioFileMetadata": {
                "name": "song",
                "duration": 600
            }
        }
        response = self.client.post(self.create_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AudioListTestCase(APITestCase):

    def setUp(self):
        serializer = SongSerializer(data={
            "name": "song",
            "duration": 600
        })
        if serializer.is_valid():
            serializer.save()

        serializer = PodcastSerializer(data={
            "name": "podcast",
            "duration": 600,
            "host": "host 1",
            "participants": "person1, person2, person3, person4, person5, person6, person7"
        })
        if serializer.is_valid():
            serializer.save()

        serializer = AudiobookSerializer(data={
            "name": "audiobook",
            "author": "author 1",
            "narrator": "narrator 1",
            "duration": 600
        })
        if serializer.is_valid():
            serializer.save()

    def test_song_list_ideal(self):
        list_url = reverse('list', kwargs={"audioFileType": 'song'})
        response = self.client.get(list_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_list_ideal_with_song_id(self):
        list_url = reverse('list', kwargs={"audioFileType": 'song'})
        response = self.client.get(list_url + "?audioFileID=1")
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_list_ideal_with_song_id_404(self):
        list_url = reverse('list', kwargs={"audioFileType": 'song'})
        response = self.client.get(list_url + "?audioFileID=2")
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_podcast_list_ideal(self):
        list_url = reverse('list', kwargs={"audioFileType": 'podcast'})
        response = self.client.get(list_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_list_ideal_with_song_id(self):
        list_url = reverse('list', kwargs={"audioFileType": 'podcast'})
        response = self.client.get(list_url + "?audioFileID=1")
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_list_ideal_with_song_id_404(self):
        list_url = reverse('list', kwargs={"audioFileType": 'podcast'})
        response = self.client.get(list_url + "?audioFileID=2")
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_audiobook_list_ideal(self):
        list_url = reverse('list', kwargs={"audioFileType": 'audiobook'})
        response = self.client.get(list_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobook_list_ideal_with_song_id(self):
        list_url = reverse('list', kwargs={"audioFileType": 'audiobook'})
        response = self.client.get(list_url + "?audioFileID=1")
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobook_list_ideal_with_song_id_404(self):
        list_url = reverse('list', kwargs={"audioFileType": 'audiobook'})
        response = self.client.get(list_url + "?audioFileID=2")
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_audioFileType_wrong_type(self):
        list_url = reverse('list', kwargs={"audioFileType": 'wrong_type'})
        response = self.client.get(list_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AudioDeleteTestCase(APITestCase):

    def setUp(self):
        serializer = SongSerializer(data={
            "name": "song",
            "duration": 600
        })
        if serializer.is_valid():
            serializer.save()

        serializer = PodcastSerializer(data={
            "name": "podcast",
            "duration": 600,
            "host": "host 1",
            "participants": "person1, person2, person3, person4, person5, person6, person7"
        })
        if serializer.is_valid():
            serializer.save()

        serializer = AudiobookSerializer(data={
            "name": "audiobook",
            "author": "author 1",
            "narrator": "narrator 1",
            "duration": 600
        })
        if serializer.is_valid():
            serializer.save()

    def test_song_delete_ideal_with_song_id(self):
        delete_url = reverse('delete', kwargs={"audioFileType": 'song', "audioFileID": 1})
        response = self.client.delete(delete_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_delete_ideal_with_song_id(self):
        delete_url = reverse('delete', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        response = self.client.delete(delete_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobook_delete_ideal_with_song_id(self):
        delete_url = reverse('delete', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        response = self.client.delete(delete_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobook_delete_ideal_with_song_id_404(self):
        delete_url = reverse('delete', kwargs={"audioFileType": 'audiobook', "audioFileID": 2})
        response = self.client.delete(delete_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_audioFileType_wrong_type(self):
        delete_url = reverse('delete', kwargs={"audioFileType": 'wrong_type', "audioFileID": 2})
        response = self.client.delete(delete_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AudioUpdateTestCase(APITestCase):

    def setUp(self):
        serializer = SongSerializer(data={
            "name": "song",
            "duration": 600
        })
        if serializer.is_valid():
            serializer.save()

        serializer = PodcastSerializer(data={
            "name": "podcast",
            "duration": 600,
            "host": "host 1",
            "participants": "person1, person2, person3, person4, person5, person6, person7"
        })
        if serializer.is_valid():
            serializer.save()

        serializer = AudiobookSerializer(data={
            "name": "audiobook",
            "author": "author 1",
            "narrator": "narrator 1",
            "duration": 600
        })
        if serializer.is_valid():
            serializer.save()

    def test_song_update_ideal_with_song_id(self):
        update_url = reverse('update', kwargs={"audioFileType": 'song', "audioFileID": 1})
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_update_name_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'song', "audioFileID": 1})
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_song_update_duration_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'song', "audioFileID": 1})
        data = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song new",
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_update_ideal_with_song_id(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast new",
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_update_name_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_update_duration_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast new",
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_update_host_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast new",
                "duration": 600,
                "participants": "person1, person2, person3, person4, person5, person6, person7"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_update_participants_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast new",
                "duration": 600,
                "host": "host 1"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_podcast_update_participants_greater_than_10(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast new",
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4, person5,"
                                "person6, person7, person8, person9, person10, person11"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_podcast_update_psrticipants_name_greater_than_100_char(self):
        update_url = reverse('update', kwargs={"audioFileType": 'podcast', "audioFileID": 1})
        data = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast new",
                "duration": 600,
                "host": "host 1",
                "participants": "person1, person2, person3, person4 person4 person4 person4person4 person4 person4"
                                "person4 person4 person4 person4person4 person4 person4 person4"
                                "person4 person4 person4 person4person4 person4 person4 person4"
                                "person4 person4 person4 person4, person5, person6, person7"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_update_ideal_with_song_id(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook new",
                "author": "author 1 new",
                "narrator": "narrator 1 new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobook_update_name_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "author": "author 1 new",
                "narrator": "narrator 1 new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_update_duration_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook new",
                "author": "author 1 new",
                "narrator": "narrator 1 new"
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_update_author_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook new",
                "narrator": "narrator 1 new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_update_narrator_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook new",
                "author": "author 1 new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audiobook_update_ideal_with_song_id_404(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 2})
        data = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "audiobook new",
                "author": "author 1 new",
                "narrator": "narrator 1 new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_audioFileType_wrong_type(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook 2', "audioFileID": 2})
        data = {
            "audioFileType": "audiobook 2",
            "audioFileMetadata": {
                "name": "audiobook new",
                "author": "author 1 new",
                "narrator": "narrator 1 new",
                "duration": 600
            }
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_audioFileMetadata_missing(self):
        update_url = reverse('update', kwargs={"audioFileType": 'audiobook', "audioFileID": 1})
        data = {
            "audioFileType": "audiobook",
        }
        response = self.client.put(update_url, data=data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
