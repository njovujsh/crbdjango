#  ugandaregions.py
#  
#  Copyright 2015 root <root@wangolo-OptiPlex-3020>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


class UgandanRegions(object):
    def __init__(self):
        self.central_region = ( ('Buikwe', 'Buikwe'),
                                ('Bukomansimbi ', 'Bukomansimbi'),
                                ('Butambala ', 'Butambala '),
                                ('Buvuma ', 'Buvuma '),
                                ('Gomba ', 'Gomba '),
                                ('Kalangala ', 'Kalangala '),
                                ('Kalungu ', 'Kalungu '),
                                ('Kampala ', 'Kampala '),
                                ('Kayunga ', 'Kayunga '),
                                ('Kiboga ', 'Kiboga '),
                                ('Kyankwanzi District', 'Kyankwanzi District'),
                                ('Luwero', 'Luwero'),
                                ('Lwengo ', 'Lwengo '),
                                ('Lyantonde ', 'Lyantonde '),
                                ('Masaka ', 'Masaka '),
                                ('Mityana ', 'Mityana '),
                                ('Mpigi ', 'Mpigi '),
                                ('Mubende ', 'Mubende '),
                                ('Mukono ', 'Mukono '),
                                ('Nakaseke ', 'Nakaseke '),
                                ('Nakasongola', 'Nakasongola'),
                                ('Rakai', 'Rakai'),
                                ('Sembabule', 'Sembabule'),
                                ('Wakiso', 'Wakiso'),
                                ('Entebbe Municipal Council', 'Entebbe Municipal Council'),
                                ('Mukono Municipal Council', 'Mukono Municipal Council'),
                            )
        self.northern_region = (
                                ('Abim ', 'Abim '),
                                ('Adjumani ', 'Adjumani '),
                                ('Agago ', 'Agago '),
                                ('Alebtong ', 'Alebtong '),
                                ('Amolatar ', 'Amolatar '),
                                ('Amudat ', 'Amudat '),
                                ('Amuru ', 'Amuru '),
                                ('Apac ', 'Apac '),
                                ('Arua ', 'Arua '),
                                ('Dokolo ', 'Dokolo '),
                                ('Gulu ', 'Gulu '),
                                ('Kaabong ', 'Kaabong '),
                                ('Kitgum ', 'Kitgum '),
                                ('Koboko ', 'Koboko '),
                                ('Kole ', 'Kole '),
                                ('Kotido ', 'Kotido '),
                                ('Lamwo ', 'Lamwo '),
                                ('Lira ', 'Lira '),
                                ('Maracha ', 'Maracha '),
                                ('Moroto ', 'Moroto '),
                                ('Moyo ', 'Moyo '),
                                ('Nakapiripirit ', 'Nakapiripirit '),
                                ('Napak ', 'Napak '),
                                ('Nebbi ', 'Nebbi '),
                                ('Nwoya ', 'Nwoya '),
                                ('Otuke ', 'Otuke '),
                                ('Oyam ', 'Oyam '),
                                ('Pader ', 'Pader '),
                                ('Yumbe ', 'Yumbe '),
                                ('Zombo ', 'Zombo '),
                            )
        
        self.western_region = (
                                ('Buhweju ', 'Buhweju'),
                                ('Buliisa ', 'Buliisa '),
                                ('Bundibugyo ', 'Bundibugyo '),
                                ('Bushenyi ', 'Bushenyi '),
                                ('Hoima ', 'Hoima '),
                                ('Ibanda ', 'Ibanda '),
                                ('Isingiro ', 'Isingiro '),
                                ('Kabale ', 'Kabale '),
                                ('Kabarole ', 'Kabarole '),
                                ('Kamwenge ', 'Kamwenge '),
                                ('Kanungu ', 'Kanungu '),
                                ('Kasese ', 'Kasese'),
                                ('Kibaale ', 'Kibaale'),
                                ('Kiruhura ', 'Kiruhura'),
                                ('Kiryandongo ', 'Kiryandongo'),
                                ('Kisoro ', 'Kisoro'),
                                ('Kyegegwa', 'Kyegegwa'),
                                ('Kyenjojo', 'Kyenjojo'),
                                ('Masindi', 'Masindi'),
                                ('Mbarara', 'Mbarara'),
                                ('Mitooma', 'Mitooma'),
                                ('Ntoroko', 'Ntoroko'),
                                ('Ntungamo', 'Ntungamo'),
                                ('Rubirizi', 'Rubirizi'),
                                ('Rukungiri', 'Rukungiri'),
                                ('Sheema ', 'Sheema'),
                                ('Hoima Municipal Council', 'Hoima Municipal Council'),
                                ('Kasese Municipal Council', 'Kasese Municipal Council'),
                                ('Rukungiri Municipal Council', 'Rukungiri Municipal Council'),
                                ('Masindi Municipal Council', 'Masindi Municipal Council'),
                                ('Mbarara Municipal Council', 'Mbarara Municipal Council'),
                                ('Bushenyi Ishaka Municipal Council', 'Bushenyi Ishaka Municipal Council'),
                                ('Arua Municipal Council', 'Arua Municipal Council'),
                                ('Moroto Municipal Council', 'Moroto Municipal Council'),
                                ('Lira Municipal Council', 'Lira Municipal Council'),
                                ('Gulu Municipal Council', 'Gulu Municipal Council'),
                            )
        
        self.estern_region = (
                            ('Amuria ', 'Amuria '),
                            ('Budaka ', 'Budaka '),
                            ('Bududa ', 'Bududa '),
                            ('Bugiri ', 'Bugiri '),
                            ('Bukedea ', 'Bukedea '),
                            ('Bukwa ', 'Bukwa '),
                            ('Bulambuli ', 'Bulambuli '),
                            ('Busia ', 'Busia '),
                            ('Butaleja ', 'Butaleja '),
                            ('Buyende ', 'Buyende '),
                            ('Iganga ', 'Iganga '),
                            ('Jinja ', 'Jinja '),
                            ('Kaberamaido ', 'Kaberamaido '),
                            ('Kaliro ', 'Kaliro '),
                            ('Kamuli ', 'Kamuli '),
                            ('Kapchorwa ', 'Kapchorwa '),
                            ('Katakwi ', 'Katakwi '),
                            ('Kibuku ', 'Kibuku '),
                            ('Kumi ', 'Kumi '),
                            ('Kween ', 'Kween '),
                            ('Luuka ', 'Luuka '),
                            ('Manafwa', 'Manafwa '),
                            ('Mayuge', 'Mayuge '),
                            ('Mbale', 'Mbale '),
                            ('Namayingo', 'Namayingo '),
                            ('Namutumba', 'Namutumba '),
                            ('Ngora', 'Ngora '),
                            ('Pallisa', 'Pallisa '),
                            ('Serere', 'Serere '),
                            ('Sironko', 'Sironko '),
                            ('Soroti', 'Soroti '),
                            ('Tororo', 'Tororo '),
                            ('TororoZone', 'TororoZone '),
                            ('Busia Municipal Council', 'Busia Municipal Council'),
                            ('Tororo Municipal Council', 'Tororo Municipal Council'),
                            ('Mbale Municipal Council', 'Mbale Municipal Council'),
                    )
                    
        
        self.all_regions = {"Central Region":self.central_region, "Northern":self.northern_region, "Western":self.western_region,
                            "Eastern":self.estern_region
                            }
                            
    def _tuple_2_dict(self, t):
        """
        Convert the given tuple into a dictionary.
        """
        self.dictionary = {}
        if(isinstance(t, tuple)):
            for tuple_item in t:
                for index, item in enumerate(tuple_item):
                    self.dictionary[tuple_item[index].strip()] = tuple_item[index].strip()
            return self.dictionary
        else:
            return False 
            
    def _get_regions(self, region):
        if(len(region)):
            return self.all_regions.get(region)
        else:
            return False 
        
    def get_region_indict(self, region):
        try:
            self.region = self._get_regions(region)
            if(self.region):
                return self._tuple_2_dict(self.region)
        except:
            raise 
            
    def search_in_region(self, region, district):
        try:
            self.region = self._get_regions(region)
            if(self.region):
                self.region_dict = self._tuple_2_dict(self.region)
                if(self.region_dict):
                    return self.region_dict.get(district)
        except:
            raise 
            
