from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from api.models import Song, Podcast, Audiobook, AUDIO_FILE_TYPE
from api.serializers import SongSerializer, PodcastSerializer, AudiobookSerializer


@api_view(['POST'])
def audio_create(request):
    file_type = request.data.get('audioFileType')
    meta = request.data.get('audioFileMetadata')

    if file_type and meta:
        if file_type in AUDIO_FILE_TYPE:
            try:
                serializer = ''
                if file_type == Song.TYPE:
                    serializer = SongSerializer(data=meta)
                elif file_type == Podcast.TYPE:
                    serializer = PodcastSerializer(data=meta)
                elif file_type == Audiobook.TYPE:
                    serializer = AudiobookSerializer(data=meta)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': ErrorDetail('audioFileType available choice are ' + str(AUDIO_FILE_TYPE),
                                                  code='required')},
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': ErrorDetail('audioFileType and audioFileMetadata', code='required')},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def audio_list(request, audioFileType):
    audioFileID = request.GET.get('audioFileID')
    if audioFileType in AUDIO_FILE_TYPE:
        serializer = None
        if audioFileType == Song.TYPE:
            if audioFileID:
                try:
                    songs = Song.objects.get(id=audioFileID)
                    serializer = SongSerializer(songs)
                except:
                    pass
            else:
                songs = Song.objects.all()
                serializer = SongSerializer(songs, many=True)
        elif audioFileType == Podcast.TYPE:
            if audioFileID:
                try:
                    podcasts = Podcast.objects.get(id=audioFileID)
                    serializer = PodcastSerializer(podcasts)
                except:
                    pass
            else:
                podcasts = Podcast.objects.all()
                serializer = PodcastSerializer(podcasts, many=True)
        elif audioFileType == Audiobook.TYPE:
            if audioFileID:
                try:
                    audios = Audiobook.objects.get(id=audioFileID)
                    serializer = AudiobookSerializer(audios)
                except:
                    pass
            else:
                audios = Audiobook.objects.all()
                serializer = AudiobookSerializer(audios, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': ErrorDetail('audioFileID {} is not exist.'.format(audioFileID),
                                                  code='required')},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': ErrorDetail('audioFileType available choice are ' + str(AUDIO_FILE_TYPE),
                                              code='required')},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def audio_delete(request, audioFileType, audioFileID):
    if audioFileType in AUDIO_FILE_TYPE:
        audioFile_obj = None
        if audioFileType == Song.TYPE:
            try:
                audioFile_obj = Song.objects.get(id=audioFileID)
            except:
                pass
        if audioFileType == Podcast.TYPE:
            try:
                audioFile_obj = Podcast.objects.get(id=audioFileID)
            except:
                pass
        if audioFileType == Audiobook.TYPE:
            try:
                audioFile_obj = Audiobook.objects.get(id=audioFileID)
            except:
                pass
        if audioFile_obj:
            audioFile_obj.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': ErrorDetail('audioFileID {} is not exist.'.format(audioFileID),
                                                  code='required')},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': ErrorDetail('audioFileType available choice are ' + str(AUDIO_FILE_TYPE),
                                              code='required')},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def audio_update(request, audioFileType, audioFileID):
    meta = request.data.get('audioFileMetadata')
    if meta:
        if audioFileType in AUDIO_FILE_TYPE:
            try:
                serializer = None
                audioFile_obj = None
                if audioFileType == Song.TYPE:
                    try:
                        audioFile_obj = Song.objects.get(id=audioFileID)
                        serializer = SongSerializer(audioFile_obj, data=meta)
                    except:
                        pass
                if audioFileType == Podcast.TYPE:
                    try:
                        audioFile_obj = Podcast.objects.get(id=audioFileID)
                        serializer = PodcastSerializer(audioFile_obj, data=meta)
                    except:
                        pass
                if audioFileType == Audiobook.TYPE:
                    try:
                        audioFile_obj = Audiobook.objects.get(id=audioFileID)
                        serializer = AudiobookSerializer(audioFile_obj, data=meta)
                    except:
                        pass
                if audioFile_obj:
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        # print(serializer.errors)
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': ErrorDetail('audioFileID {} is not exist.'.format(audioFileID),
                                                          code='required')},
                                    status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': ErrorDetail('audioFileType available choice are ' + str(AUDIO_FILE_TYPE),
                                                  code='required')},
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': ErrorDetail('audioFileMetadata', code='required')},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def page_404(request):
    return Response(status=status.HTTP_404_NOT_FOUND)