from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(required=True, max_length=15)
    gender = serializers.ChoiceField(choices=[('M', '남성'), ('F', '여성')], required=True)
    age = serializers.IntegerField(required=True, min_value=0)
    profile_image = serializers.ImageField(required=False)
    introduction = serializers.CharField(required=False, allow_blank=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['email'] = self.validated_data.get('email', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        data['gender'] = self.validated_data.get('gender', '')
        data['age'] = self.validated_data.get('age', None)
        data['profile_image'] = self.validated_data.get('profile_image', None)
        data['introduction'] = self.validated_data.get('introduction', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.email = self.validated_data.get('email', '')
        user.nickname = self.validated_data.get('nickname', '')
        user.gender = self.validated_data.get('gender', '')
        user.age = self.validated_data.get('age', None)
        user.profile_image = self.validated_data.get('profile_image', None)
        user.introduction = self.validated_data.get('introduction', '')
        user.save()
        return user