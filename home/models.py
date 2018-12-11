from dateutil.relativedelta import *
from datetime import date
from django.db import models
from django.db.models import CASCADE
from multiselectfield import MultiSelectField

from accounts.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)


class Child(models.Model):

    EU_SIZES_DICT = {
        '32': 0, '38': 1, '44': 2, '50': 3, '56': 4, '62': 5, '68': 6, '74': 7, '80': 8, '86': 9, '92': 10, '98': 11,
        '104': 12, '110': 13, '116': 14, '122': 15, '128': 16, '134': 17, '140': 18, '146': 19, '152': 20
    }

    CLOTHING_SIZES = {
        'EU': ((0, '32'), (1, '38'), (2, '44'), (3, '50'), (4, '56'), (5, '62'), (6, '68'), (7, '74'), (8, '80'),
               (9, '86'), (10, '92'), (11, '98'), (12, '104'), (13, '110'), (14, '116'), (15, '122'), (16, '128'),
               (17, '134'), (18, '140'), (19, '146'), (20, '152')),
        'UK': ((0, ''), (1, ''), (2, ''), (3, ''), (4, '0m'), (5, '3m'), (6, '6m'), (7, '9m'), (8, '12m'),
               (9, '18m'), (10, '24m'), (11, '2'), (12, '3'), (13, '4'), (14, '5'), (15, '6'), (16, '7'),
               (17, '8'), (18, '9'), (19, '10'), (20, '11'), (21, '12')),
        'US': ((0, ''), (1, ''), (2, ''), (3, 'new3'), (4, '0m'), (5, '3m'), (6, '6m'), (7, '9m'), (8, '12m'),
               (9, '18m'), (10, '24m'), (11, '2T'), (12, '3T'), (13, '4T'), (14, '5'), (15, '6'), (16, '6X-7'),
               (17, '8'), (18, '9'), (19, '10'), (20, '11'), (21, '14')),
    }

    SHOE_SIZES = {
        'EU': ((0, ''), (1, '16'), (2, '17'), (3, '18'), (4, '19'), (5, '19.5'), (6, '20.5'), (7, '21'), (8, '21.5'),
               (9, '22'), (10, '23'), (11, '23.5'), (12, '24'), (13, '25'), (14, '25.5'), (15, '26'), (16, '26.5'),
               (17, '27.5'), (18, '28'), (19, '28.5'), (20, '29'), (21, '30'), (22, '30.5'), (23, '31'), (24, '32'),
               (25, '32.5'), (26, '33'), (27, '33.5'), (28, '34.5'), (29, '35'), (30, '35.5'), (31, '36'), (32, '37'),
               (33, '37.5'), (34, '38'), (35, '38.5'), (36, '39'), (37, '40'), (38, '41'), (39, '41.5'), (40, '42')),
        'UK': ((0, ''), (1, ''), (2, ''), (3, ''), (4, '3'), (5, '3.5'), (6, '4'), (7, '4.5'), (8, '5'),
               (9, '5.5'), (10, '6'), (11, '6.5'), (12, '7'), (13, '7.5'), (14, '8'), (15, '8.5'), (16, '9'),
               (17, '9.5'), (18, '10'), (19, '10.5'), (20, '11'), (21, '11.5'), (22, '12'), (23, '12.5'), (24, '13'),
               (25, '13.5'), (26, '1'), (27, '1.5'), (28, '2'), (29, '2.5'), (30, '3'), (31, '3.5'), (32, '4'),
               (33, '4.5'), (34, '5'), (35, '5.5'), (36, '6'), (37, '6.5'), (38, '7'), (39, '7.5'), (40, '8')),
        'US': ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '4.5'), (6, '5'), (7, '5.5'), (8, '6'),
               (9, '6.5'), (10, '7'), (11, '7.5'), (12, '8'), (13, '8.5'), (14, '9'), (15, '9.5'), (16, '10'),
               (17, '10.5'), (18, '11'), (19, '11.5'), (20, '12'), (21, '12.5'), (22, '13'), (23, '13.5'), (24, '1'),
               (25, '1.5'), (26, '2'), (27, '2.5'), (28, '3'), (29, '3.5'), (30, '4'), (31, '4.5'), (32, '5'),
               (33, '5.5'), (34, '6'), (35, '6.5'), (36, '7'), (37, '7.5'), (38, '8'), (39, '8.5'), (40, '9')),
    }

    F, P, N = "F", "P", "Not born yet"
    CHILD_STATUS_CHOICES = (
        (F, "Full term"),
        (P, "Preemie"),
        (N, 'Not born yet'),
    )

    CHILD_GENDER_CHOICES = (
        ("BOY", 'Boy'),
        ("GIRL", 'Girl'),
    )

    EU, UK, US = 'EU', "UK", "US"
    SIZE_SYSTEMS = (
        (EU, "EU"),
        (UK, "UK"),
        (US, "US"),
    )

    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=5, choices=CHILD_GENDER_CHOICES, default=None, blank=True, null=True)
    picture = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg', blank=True)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    size_system = models.CharField(max_length=5, choices=SIZE_SYSTEMS, default="EU")
    child_status = models.CharField(max_length=15, choices=CHILD_STATUS_CHOICES, default="F")
    due_date = models.DateField(default=None, blank=True, null=True)

    CORRECTED_SIZE_CHOICES = ((0, '32'), (1, '38'), (2, '44'),
                              (3, '50'), (4, '56'), (5, '62'),
                              (6, '68'), (7, '74'), (8, '80'),
                              (9, '86'), (10, '92'), (11, '98'),
                              (12, '104'), (13, '110'), (14, '116'),
                              (15, '122'), (16, '128'), (17, '134'),
                              (18, '140'), (19, '146'), (20, '152'))
    corrected_sizes = MultiSelectField(choices=CORRECTED_SIZE_CHOICES, max_choices=3, default=None, blank=True, null=True)

    @property
    def sizes(self):
        return self.CLOTHING_SIZES.get(self.size_system)

    @property
    def shoe_sizes(self):
        return self.SHOE_SIZES.get(self.size_system)

    @property
    def age(self):
        today = date.today()
        if self.date_of_birth is not None:
            age = relativedelta(today, date(self.date_of_birth.year, self.date_of_birth.month, self.date_of_birth.day))
            return age
        else:
            return

    @property
    def clothes_size(self):

        if self.age.years == 0 and self.age.months == 0:
            return self.sizes[3][1], self.sizes[4][1]

        if self.age.years == 0 and 3 > self.age.months >= 1:
            return self.get_size(0, 3, self.sizes[4][1], self.sizes[5][1])

        if self.age.years == 0 and 6 > self.age.months >= 3:
            return self.get_size(3, 6, self.sizes[5][1], self.sizes[6][1])

        if self.age.years == 0 and 9 > self.age.months >= 6:
            return self.get_size(6, 9, self.sizes[6][1], self.sizes[7][1])

        if self.age.years == 0 and 12 > self.age.months >= 9:
            return self.get_size(9, 12, self.sizes[7][1], self.sizes[8][1])

        if self.age.years == 1 and 6 > self.age.months >= 0:
            return self.get_size(0, 6, self.sizes[8][1], self.sizes[9][1])

        if self.age.years == 1 and 12 > self.age.months >= 6:
            return self.get_size(6, 12, self.sizes[9][1], self.sizes[10][1])

        if self.age.years == 2 and 12 > self.age.months >= 0:
            return self.get_size(0, 12, self.sizes[10][1], self.sizes[11][1])

        if 4 >= self.age.years >= 3:
            return self.get_size(0, 0, self.sizes[11][1], self.sizes[12][1], 3, 4)

        if 5 >= self.age.years >= 4:
            return self.get_size(0, 0, self.sizes[12][1], self.sizes[13][1], 4, 5)

        if 6 >= self.age.years >= 5:
            return self.get_size(0, 0, self.sizes[13][1], self.sizes[14][1], 5, 6)

        if 7 >= self.age.years >= 6:
            return self.get_size(0, 0, self.sizes[14][1], self.sizes[15][1], 6, 7)

        if 8 >= self.age.years >= 7:
            return self.get_size(0, 0, self.sizes[15][1], self.sizes[16][1], 7, 8)

        if 9 >= self.age.years >= 8:
            return self.get_size(0, 0, self.sizes[16][1], self.sizes[17][1], 8, 9)

        if 10 >= self.age.years >= 9:
            return self.get_size(0, 0, self.sizes[17][1], self.sizes[18][1], 9, 10)

        if 11 >= self.age.years >= 10:
            return self.get_size(0, 0, self.sizes[18][1], self.sizes[19][1], 10, 11)

        if 12 >= self.age.years >= 11:
            return self.get_size(0, 0, self.sizes[19][1], self.sizes[20][1], 11, 12)

    # Just the string representation
    def get_clothes_sizes_str(self):
        if self.clothes_size:
            if type(self.clothes_size) is tuple:
                return f"{self.clothes_size[0]} - {self.clothes_size[1]}"
            else:
                return f"{self.clothes_size}"

    # It is used many times in the clothes_size() property.
    # It returns the right size based on the which part of the period (the beginning, the end or the middle)
    def get_size(self, first_month, last_month, first_size, second_size, first_year=0, second_year=0):
        if first_year and second_year:
            if self.age.years == first_year and 0 <= self.age.months <= 6:
                return first_size
            if self.age.years == first_year and 6 < self.age.months <= 12:
                return first_size, second_size
            if self.age.years == second_year and 0 <= self.age.months <= 6:
                return first_size, second_size
            if self.age.years == second_year and 6 < self.age.months <= 12:
                return second_size
        else:
            if first_month <= self.age.months <= (first_month + ((last_month - first_month) / 3 - 1)):
                return first_size
            if (last_month - ((last_month - first_month) / 3 - 1)) <= self.age.months <= last_month:
                return second_size
            if (first_month + (last_month - first_month) / 3 - 1) < \
                    self.age.months < (last_month - ((last_month - first_month) / 3 - 1)):
                return first_size, second_size

    """sd(size difference) Returns the difference between the estimated size and the real one"""
    def sd(self):
        if self.corrected_sizes is not None:
            if type(self.clothes_size) is tuple:
                estimated_size2 = self.EU_SIZES_DICT.get(str(self.clothes_size[1]))

                if len(self.corrected_sizes) == 1:
                    corrected_size = self.corrected_sizes[0][0]
                    return corrected_size - estimated_size2

                elif len(self.corrected_sizes) == 2:
                    corrected_size2 = self.corrected_sizes[1][0]
                    return corrected_size2 - estimated_size2

                elif len(self.corrected_sizes) == 3:
                    corrected_size3 = self.corrected_sizes[2][0]
                    return corrected_size3 - estimated_size2

            else:
                estimated_size = self.EU_SIZES_DICT.get(str(self.clothes_size))

                if len(self.corrected_sizes) == 1:
                    corrected_size = self.corrected_sizes[0][0]
                    return corrected_size - estimated_size

                elif len(self.corrected_sizes) == 2:
                    corrected_size2 = self.corrected_sizes[1][0]
                    return corrected_size2 - estimated_size

                elif len(self.corrected_sizes) == 3:
                    corrected_size1 = self.corrected_sizes[0][0]
                    corrected_size2 = self.corrected_sizes[1][0]
                    corrected_size3 = self.corrected_sizes[2][0]

                    if corrected_size2 == estimated_size:
                        return 0
                    elif corrected_size1 >= estimated_size:
                        return estimated_size - corrected_size1
                    elif corrected_size3 <= estimated_size:
                        return estimated_size - corrected_size3

        else:  # if there is no corrected sizes
            # if self.baby_status == "Preemie":
            pass

