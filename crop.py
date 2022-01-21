#############################################
# Barabas Maximilian / Szoft I N / 2022.01.21
#############################################


#crop.py
from cropModel import CropModel
from typing import List

class Crop:
    def __init__(self):
        self.file_name = 'termes.txt'
        self.crops: List[CropModel] = []

    def read_content(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines() 
        fp.close()
    
    
    def convert_content(self):        
        for line in self.lines[1:]:
            (id, name, place, size, cropyield, year) = line.split(':')
            cropModel = CropModel(
                id, 
                name, 
                place, 
                int(size),
                float(cropyield.replace(',','.') ), 
                int(year)
                )
            self.crops.append(cropModel)


    # Földterület összesen
    def total_land(self):
        pass

    # Hány tonna búza termés volt összesen?
    def sum_wheat(self):
        pass

    # 300-nál több termés esetén név és termés legyen kiírtva
    def more_then_three_hundred(self):
        pass

    # Hány területen termelnek árpát?
    def area_barley(self):
        pass

    # Hány terület nagyobb mint 80 hektár?
    def area_larger_eighty(self):
        pass
    

    # Milyen gabona termett a "Csendes" nevű területen?
    def which_crop_on_csendes(self):
        pass
    
    # Melyik területről lett a legkevesebb búzatermés?
    def which_place_wheat_min(self):
        pass

crop = Crop()
crop.read_content()
crop.convert_content()
crop.total_land()
crop.more_then_three_hundred()
crop.area_barley()
crop.area_larger_eighty()
crop.which_crop_on_csendes()
crop.which_place_wheat_min()