#  checkenforcements.py
#  
#  Copyright 2015 Wangolo Joel <wangolo@developer>
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
from validators.subsystems.enforcements import enf001
from validators.subsystems.enforcements import enf002
from validators.subsystems.enforcements import enf003
from validators.subsystems.enforcements import enf004
from validators.subsystems.enforcements import enf013
from validators.subsystems.enforcements import enf068
from validators.subsystems.enforcements import enf069
from validators.subsystems.enforcements import enf014
from validators.subsystems.enforcements import enf071
from validators.subsystems.enforcements import enf070
from validators.subsystems.enforcements import enf030
from validators.subsystems.enforcements import enf061
from validators.subsystems.enforcements import enf007
from validators.subsystems.enforcements import enf042
from validators.subsystems.enforcements import enf043
from validators.subsystems.enforcements import enf037
from validators.subsystems.enforcements import enf094
from validators.subsystems.enforcements import enf050
from validators.subsystems.enforcements import enf057
from validators.subsystems.enforcements import enf080
from validators.subsystems.enforcements import enf082
from validators.subsystems.enforcements import enf078
from validators.subsystems.enforcements import enf079
from validators.subsystems.enforcements import enf071
from validators.subsystems.enforcements import enf081
from validators.subsystems.enforcements import enf047
from validators.subsystems.enforcements import enf083
from validators.subsystems.enforcements import enf051
from validators.subsystems.enforcements import enf052
from validators.subsystems.enforcements import enf029
from validators.subsystems.enforcements import enf025
from validators.subsystems.enforcements import enf028
from validators.subsystems.enforcements import enf015
from validators.subsystems.enforcements import enf024
from validators.subsystems.enforcements import enf023
from validators.subsystems.enforcements import enf017
from validators.subsystems.enforcements import enf021
from validators.subsystems.enforcements import enf056
from validators.subsystems.enforcements import enf084
from validators.subsystems.enforcements import enf065
from validators.subsystems.enforcements import enf064
from validators.subsystems.enforcements import enf093
from validators.subsystems.enforcements import enf095
from validators.subsystems.enforcements import enf092
from validators.subsystems.enforcements import enf096
from validators.subsystems.enforcements import enf097
from validators.subsystems.enforcements import enf012
from validators.subsystems.enforcements import enf087
from validators.subsystems.enforcements import enf027
from validators.subsystems.enforcements import enf088
from validators.subsystems.enforcements import enf089
from validators.subsystems.enforcements import enf090
from validators.subsystems.enforcements import enf098
from validators.subsystems.enforcements import enf099
from validators.subsystems.enforcements import enf100
from validators.subsystems.enforcements import enf101
from validators.subsystems.enforcements import enf102
from validators.subsystems.enforcements import enf103
from validators.subsystems.enforcements import enf104
from validators.subsystems.enforcements import enf105
from validators.subsystems.enforcements import enf106
from validators.subsystems.enforcements import enf107
from validators.subsystems.enforcements import enf108
from validators.subsystems.enforcements import enf109
from validators.subsystems.enforcements import enf110
from validators.subsystems.enforcements import enf112
from validators.subsystems.enforcements import enf005
from validators.subsystems.enforcements import enf006
from validators.subsystems.enforcements import enf008
from validators.subsystems.enforcements import enf009
from validators.subsystems.enforcements import enf010
from validators.subsystems.enforcements import enf011
from validators.subsystems.enforcements import enf016
from validators.subsystems.enforcements import enf018
from validators.subsystems.enforcements import enf019
from validators.subsystems.enforcements import enf020
from validators.subsystems.enforcements import enf022
from validators.subsystems.enforcements import enf035
from validators.subsystems.enforcements import enf085
from validators.subsystems.enforcements import enf066
from validators.subsystems.enforcements import enf053
from validators.subsystems.enforcements import enf059
from validators.subsystems.enforcements import enf026
from validators.subsystems.enforcements import enf048
from validators.subsystems.enforcements import enf060
from validators.subsystems.enforcements import enf067
from validators.subsystems.enforcements import enf086
from validators.subsystems.enforcements import enf055

#Fortys
from validators.subsystems.enforcements import enf040
from validators.subsystems.enforcements import enf046
from validators.subsystems.enforcements import enf033
from validators.subsystems.enforcements import enf062
from validators.subsystems.enforcements import enf034
from validators.subsystems.enforcements import enf077
from validators.subsystems.enforcements import enf091
from validators.subsystems.enforcements import enf045
from validators.subsystems.enforcements import enf044
from validators.subsystems.enforcements import enf032
from validators.subsystems.enforcements import enf111
from validators.subsystems.enforcements import enf075
from validators.subsystems.enforcements import enf039
from validators.subsystems.enforcements import enf074
from validators.subsystems.enforcements import enf073
from validators.subsystems.enforcements import enf041
from validators.subsystems.enforcements import enf058
from validators.subsystems.enforcements import enf072
from validators.subsystems.enforcements import enf076
from validators.subsystems.enforcements import enf038
from validators.subsystems.enforcements import enf036
from validators.subsystems.enforcements import enf049
from validators.subsystems.enforcements import enf054

def check_enforcements(enf, model, field, priority=None):
    """
    Given the enforcements check and find the corresponding
    values and fields to validate against.
    """
    try:
        if(enf == "ENF001"):
            return enf001.ENF001(model, field, priority, None)
        elif(enf == "ENF035"):
            return enf035.ENF035(model, field, priority, None)
        elif(enf == "ENF055"):
            return enf055.ENF055(model, field, priority, None)
        elif(enf == "ENF086"):
            return enf086.ENF086(model, field, priority, None)
        elif(enf == "ENF067"):
            return enf067.ENF067(model, field, priority, None)
        elif(enf == "ENF060"):
            return enf060.ENF060(model, field, priority, None)
        elif(enf == "ENF048"):
            return enf048.ENF048(model, field, priority, None)
        elif(enf == "ENF026"):
            return enf026.ENF026(model, field, priority, None)
        elif(enf == "ENF059"):
            return enf059.ENF059(model, field, priority, None)
        elif(enf == "ENF085"):
            return enf085.ENF085(model, field, priority, None)
        elif(enf == "ENF053"):
            return enf053.ENF053(model, field, priority, None)
        elif(enf == "ENF066"):
            return enf066.ENF066(model, field, priority, None)
        elif(enf == "ENF002"):
            return enf002.ENF002(model, field, priority, None)
        elif(enf == "ENF068"):
            return enf068.ENF068(model, field, priority, None)
        elif(enf == "ENF069"):
            return enf069.ENF069(model, field, priority, None)
        elif(enf == "ENF014"):
            return enf014.ENF014(model, field, priority, None) 
        elif(enf == "ENF071"):
            return enf071.ENF071(model, field, priority, None)
        elif(enf == "ENF030"):
            return enf030.ENF030(model, field, priority, None)
        elif(enf == "ENF061"):
            return enf061.ENF061(model, field, priority, None)
        elif(enf == "ENF070"):
            return enf070.ENF070(model, field, priority, None)
        elif(enf == "ENF007"):
            return enf007.ENF007(model, field, priority, None)
        elif(enf == "ENF043"):
            return enf043.ENF043(model, field, priority, None)
        elif(enf == "ENF037"):
            return enf037.ENF037(model, field, priority, None)
        elif(enf == "ENF094"):
            return enf094.ENF094(model, field, priority, None)
        elif(enf == "ENF050"):
            return enf050.ENF050(model, field, priority, None)
        elif(enf == "ENF057"):
            return enf057.ENF057(model, field, priority, None)
        elif(enf == "ENF080"):
            return enf080.ENF080(model, field, priority, None)
        elif(enf == "ENF079"):
            return enf079.ENF079(model, field, priority, None)
        elif(enf == "ENF071"):
            return enf071.ENF071(model, field, priority, None)
        elif(enf == "ENF082"):
            return enf082.ENF082(model, field, priority, None)
        elif(enf == "ENF081"):
            return enf081.ENF081(model, field, priority, None)
        elif(enf == "ENF047"):
            return enf047.ENF047(model, field, priority, None)
        elif(enf == "ENF083"):
            return enf083.ENF083(model, field, priority, None)
        elif(enf == "ENF051"):
            return enf051.ENF051(model, field, priority, None)
        elif(enf == "ENF052"):
            return enf052.ENF052(model, field, priority, None)
        elif(enf == "ENF013"):
            return enf013.ENF013(model, field, priority, None)
        elif(enf == "ENF029"):
            return enf029.ENF029(model, field, priority, None)
        elif(enf == "ENF025"):
            return enf025.ENF025(model, field, priority, None)
        elif(enf == "ENF028"):
            return enf028.ENF028(model, field, priority, None)
        elif(enf == "ENF015"):
            return enf015.ENF015(model, field, priority, None)
        elif(enf == "ENF024"):
            return enf024.ENF024(model, field, priority, None)
        elif(enf == "ENF023"):
            return enf023.ENF023(model, field, priority, None)
        elif(enf == "ENF017"):
            return enf017.ENF017(model, field, priority, None)
        elif(enf == "ENF021"):
            return enf021.ENF021(model, field, priority, None)
        elif(enf == "ENF056"):
            return enf056.ENF056(model, field, priority, None)
        elif(enf == "ENF084"):
            return enf084.ENF084(model, field, priority, None)
        elif(enf == "ENF065"):
            return enf065.ENF065(model, field, priority, None)
        elif(enf == "ENF093"):
            return enf093.ENF093(model, field, priority, None)
        elif(enf == "ENF095"):
            return enf095.ENF095(model, field, priority, None)
        elif(enf == "ENF092"):
            return enf092.ENF092(model, field, priority, None)
        elif(enf == "ENF096"):
            return enf096.ENF096(model, field, priority, None)
        elif(enf == "ENF097"):
            return enf097.ENF097(model, field, priority, None)
        elif(enf == "ENF012"):
            return enf012.ENF012(model, field, priority, None)
        elif(enf == "ENF087"):
            return enf087.ENF087(model, field, priority, None)
        elif(enf == "ENF027"):
            return enf027.ENF027(model, field, priority, None)
        elif(enf == "ENF088"):
            return enf088.ENF088(model, field, priority, None)
        elif(enf == "ENF089"):
            return enf089.ENF089(model, field, priority, None)
        elif(enf == "ENF090"):
            return enf090.ENF090(model, field, priority, None)
        elif(enf == "ENF098"):
            return enf098.ENF098(model, field, priority, None)
        elif(enf == "ENF099"):
            return enf099.ENF099(model, field, priority, None)
        elif(enf == "ENF100"):
            return enf100.ENF100(model, field, priority, None)
        elif(enf == "ENF101"):
            return enf101.ENF101(model, field, priority, None)
        elif(enf == "ENF102"):
            return enf102.ENF102(model, field, priority, None)
        elif(enf == "ENF103"):
            return enf103.ENF103(model, field, priority, None)
        elif(enf == "ENF104"):
            return enf104.ENF104(model, field, priority, None)
        elif(enf == "ENF105"):
            return enf105.ENF105(model, field, priority, None)
        elif(enf == "ENF106"):
            return enf106.ENF106(model, field, priority, None)
        elif(enf == "ENF107"):
            return enf107.ENF107(model, field, priority, None)
        elif(enf == "ENF108"):
            return enf108.ENF108(model, field, priority, None)
        elif(enf == "ENF109"):
            return enf109.ENF109(model, field, priority, None)
        elif(enf == "ENF110"):
            return enf110.ENF110(model, field, priority, None)
        elif(enf == "ENF112"):
            return enf112.ENF112(model, field, priority, None)
        elif(enf == "ENF005"):
            return enf005.ENF005(model, field, priority, None)
        elif(enf == "ENF006"):
            return enf006.ENF006(model, field, priority, None)
        elif(enf == "ENF008"):
            return enf008.ENF008(model, field, priority, None)
        elif(enf == "ENF009"):
            return enf009.ENF009(model, field, priority, None)
        elif(enf == "ENF010"):
            return enf010.ENF010(model, field, priority, None)
        elif(enf == "ENF011"):
            return enf011.ENF011(model, field, priority, None)
        elif(enf == "ENF016"):
            return enf016.ENF016(model, field, priority, None)
        elif(enf == "ENF018"):
            return enf018.ENF018(model, field, priority, None)
        elif(enf == "ENF019"):
            return enf019.ENF019(model, field, priority, None)
        elif(enf == "ENF020"):
            return enf020.ENF020(model, field, priority, None)
        elif(enf == "ENF022"):
            return enf022.ENF022(model, field, priority, None)
        elif(enf == "ENF064"):
            return enf064.ENF064(model, field, priority, None)
        elif(enf == "ENF042"):
            return enf042.ENF042(model, field, priority, None)
        elif(enf == "ENF078"):
            return enf078.ENF078(model, field, priority, None)
        elif(enf == "ENF040"):
            return enf040.ENF040(model, field, priority, None)
        elif(enf == "ENF046"):
            return enf046.ENF046(model, field, priority, None)
        elif(enf == "ENF033"):
            return enf033.ENF033(model, field, priority, None)
        elif(enf == "ENF062"):
            return enf062.ENF062(model, field, priority, None)
        elif(enf == "ENF034"):
            return enf034.ENF034(model, field, priority, None)
        elif(enf == "ENF077"):
            return enf077.ENF077(model, field, priority, None)
        elif(enf == "ENF091"):
            return enf091.ENF091(model, field, priority, None)
        elif(enf == "ENF045"):
            return enf045.ENF045(model, field, priority, None)
        elif(enf == "ENF003"):
            return enf003.ENF003(model, field, priority, None)
        elif(enf == "ENF004"):
            return enf004.ENF004(model, field, priority, None)
        elif(enf == "ENF044"):
            return enf044.ENF044(model, field, priority, None)
        elif(enf == "ENF032"):
            return enf032.ENF032(model, field, priority, None)
        elif(enf == "ENF111"):
            return enf111.ENF111(model, field, priority, None)
        elif(enf == "ENF075"):
            return enf075.ENF075(model, field, priority, None)
        elif(enf == "ENF039"):
            return enf039.ENF039(model, field, priority, None)
        elif(enf == "ENF074"):
            return enf074.ENF074(model, field, priority, None)
        elif(enf == "ENF073"):
            return enf073.ENF073(model, field, priority, None)
        elif(enf == "ENF041"):
            return enf041.ENF041(model, field, priority, None)
        elif(enf == "ENF058"):
            return enf058.ENF058(model, field, priority, None)
        elif(enf == "ENF072"):
            return enf072.ENF072(model, field, priority, None)
        elif(enf == "ENF076"):
            return enf076.ENF076(model, field, priority, None)
        elif(enf == "ENF038"):
            return enf038.ENF038(model, field, priority, None)
        elif(enf == "ENF036"):
            return enf036.ENF036(model, field, priority, None)
        elif(enf == "ENF049"):
            return enf049.ENF049(model, field, priority, None)
        elif(enf == "ENF054"):
            return enf054.ENF054(model, field, priority, None)
        else:
            return enf001.ENF001(model, field, priority, None)
    except:
        raise 
