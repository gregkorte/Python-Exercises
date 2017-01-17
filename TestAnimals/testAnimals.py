import unittest
from animals import *

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up Animal class')
        self.animal = Animal('Bob', 'sloth')

    def test_animal_is_named(self):
        name = 'test_animal_is_named '
        self.assertEqual(self.animal.name, 'Bob', name + 'failed!!')

    def test_animal_has_species(self):
        name = 'test_animal_has_species '
        self.assertEqual(self.animal.species, 'sloth', name + 'failed!!')

    def test_can_set_animal_species(self):
        name = 'test_can_set_animal_species '
        self.animal.set_species('Greater Sloth')
        self.assertEqual(self.animal.species, 'Greater Sloth', name + 'failed!!')

    def test_animal_has_walking_speed(self):
        name = 'test_animal_has_walking_speed '
        self.animal.set_legs(2)
        self.animal.walk()
        print(self.animal)
        self.assertEqual(self.animal.speed, .2, name + 'failed!!')

    def test_animal_is_an_instance_of_Animal(self):
        if isinstance(self.animal, Animal):
            pass
        else:
            print('test_animal_is_an_instance_of_Animal failed!!')

class TestDog(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up Dog class')
        self.dog = Dog('Coco')

    def test_dog_is_named(self):
        name = 'test_dog_is_named '
        self.assertEqual(self.dog.name, 'Coco',  name + 'failed!!')

    def test_dog_has_walking_speed(self):
        name = 'test_dog_has_walking_speed '
        self.dog.set_legs(4)
        self.dog.walk()
        print(self.dog)
        self.assertEqual(self.dog.speed, .8, name + 'failed!!')

    def test_animal_is_an_instance_of_Dog(self):
        if isinstance(self.dog, Dog):
            pass
        else:
            print('test_animal_is_an_instance_of_Dog failed!!')

if __name__ == '__main__':
    unittest.main()