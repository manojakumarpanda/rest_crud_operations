from django.test import TestCase,SimpleTestCase
from .models import profile
from django.contrib.auth import get_user_model

# Create your tests here.
class Test_model(TestCase):

    @classmethod
    def setUp(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create_user(username='normaluser1', email='normal@user.com', password='password',
                                            first_name='normal', last_name='user')
        cls.super = cls.User.objects.create_superuser(username='superuser', email='super@user.com', password='password2',
                                            first_name='super', last_name='user')


    def test_user(self):
        self.assertEqual(self.user.username,'normaluser1')
        self.assertEqual(self.user.email,'normal@user.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.password)
        #for the super user
        self.assertEqual(self.super.username,'superuser')
        self.assertEqual(self.super.email,'super@user.com')
        self.assertTrue(self.super.is_active)
        self.assertTrue(self.super.is_staff)
        self.assertTrue(self.super.is_superuser)
        self.assertTrue(self.super.password)



    def test_profile(self):
        self.data=profile.objects.create(user=self.user,name='normal user',age=10,gender='M')
        self.assertEqual(self.data.user,self.user)
        self.assertEqual(self.data.name,'normal user')
        self.assertEqual(self.data.age,10)
        self.assertEqual(self.data.gender,'M')
        self.assertFalse(self.data.immage)


class Test_Url(SimpleTestCase):
    pass

class Test_View(TestCase):
    pass