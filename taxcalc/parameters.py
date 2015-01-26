import numpy as np
from .utils import expand_array


class Parameters(object):

    def __init__(self, start_year=2013, budget_years=10,
                 inflation_rate=0.2):
        self._current_year = start_year
        self._start_year = start_year

        # READ IN DATA - could read file here
        self._vals = [('_almdep', [7150, 7250, 7400]),
                      ('_almsep', [40400, 41050, ]),
                      ('_rt5', [0.33, ]),
                      ('_rt7', [0.396, ]),
                      ('_joint', [[5340, 5340, 5340, 5340], [5430, 5430, 5430, 5430], [5510, 5520, 5520, 5520]]),
                      ('_edphhs', [63, 64, 65, ]),
                      ('_agcmax', [15000, ]),
                      ('_rt3', [0.25, ]),
                      ('_thresx', [200000, 250000, 125000, 200000, 250000, 125000, ]),
                      ('_rt1', [0.1, ]),
                      ('_almdep', [7150, 7250, 7400, ]),
                      ('_brk1', [[8925, 17850, 8925, 12750, 17850, 8925], [9075, 18150, 9075, 12950, 18150, 9075], [9225, 18450, 9225, 13150, 18450, 9225]]),
                      ('_ssb85', [34000, 44000, 0, 34000, 34000, 0, ]),
                      ('_brk3', [[87850, 146400, 73200, 125450, 146400, 73200], [89350, 148850, 74425, 127550, 148850, 74425], [90750, 151200, 75600, 129600, 151200, 75600]]),
                      ('_ssb50', [25000, 32000, 0, 25000, 25000, 0, ]),
                      ('_rtless', [[0.0765, 0.1598, 0.2106, 0.2106]]),
                      ('_rt2', [0.15, ]),
                      ('_brk5', [[398350, 398350, 199175, 398350, 398350, 199175], [405100, 405100, 202550, 405100, 405100, 202550], [411500, 411500, 205750, 411500, 411500, 205750]]),
                      ('_almsp', [179500, 182500, 185400, ]),
                      ('_aged', [[1500, 1200], [1550, 1200], [1550, 1250]]),
                      ('_ssmax', [113700, 117000, 118500, ]),
                      ('_rt6', [0.35, ]),
                      ('_edphhm', [126, 128, 130, ]),
                      ('_amtex', [[51900, 80800, 40400, 51900, 80800, 40400], [52800, 82100, 41050, 52800, 82100, 41050], [53600, 83400, 41700, 53600, 83400, 41700]]),
                      ('_feimax', [97600, 99200, 100800, ]),
                      ('_rt4', [0.28, ]),
                      ('_stded', [[6100, 12200, 6100, 8950, 12200, 6100, 1000], [6200, 12400, 6200, 9100, 12400, 6200, 1000], [6300, 12600, 6300, 9250, 12600, 6300, 1050]]),
                      ('_crmax', [[487, 3250, 5372, 6044], [496, 3305, 5460, 6143], [503, 3359, 5548, 6242]]),
                      ('_pcmax', [35, ]),
                      ('_amtsep', [238550, 242450, ]),
                      ('_adctcrt', [0.15, ]),
                      ('_phase2', [[250000, 300000, 150000, 275000, 300000, 150000], [254200, 305050, 152525, 279650, 305050, 152525], [258250, 309900, 154950, 284050, 309900, 154950]]),
                      ('_brk4', [[183250, 223050, 111525, 203150, 223050, 111525], [186350, 226850, 113425, 206600, 226850, 113425], [189300, 230450, 115225, 209850, 230450, 115225]]),
                      ('_learn', [10000, ]),
                      ('_ealim', [3000, 3000, 3000, 3000, 3000, 10000, ]),
                      ('_ymax', [[7970, 17530, 17530, 17530], [8110, 17830, 17830, 17830], [8240, 18110, 18110, 18110]]),
                      ('_exmpb', [[250000, 300000, 150000, 275000, 300000, 150000], [254200, 305050, 152525, 279650, 305050, 152525], [258250, 309900, 154950, 284040, 309900, 154950]]),
                      ('_amex', [3900, 3950, 4000, ]),
                      ('_rtbase', [[0.0765, 0.34, 0.4, 0.45]]),
                      ('_brk2', [[36250, 72500, 36250, 48600, 72500, 36250], [36900, 73800, 36900, 49400, 73800, 36900], [37450, 74900, 37450, 50200, 74900, 37450]]),
                      ('_dcmax', [3000, ]),
                      ('_cgrate2', [0.2, ]),
                      ('_brk6', [[400000, 450000, 225000, 425000, 450000, 225000], [406750, 457600, 228800, 432200, 457600, 228800], [413200, 464850, 223425, 439000, 464850, 223425]]),
                      ('_cgrate1', [0.1, ]),
                      ('_dylim', [3300, 3350, 3400, ]),
                      ('_amtys', [[115400, 153900, 76950, 115400, 153900, 76950], [117300, 156500, 78250, 117300, 156500, 78250], [119200, 158900, 79450, 119200, 158900, 79450]]),
                      ('_cphase', [75000, 110000, 55000, 75000, 75000, 55000, ]),
                      ('_chmax', [1000, 1000, 1000, 1000, 1000, 500, ]),
                      ('_amtage', [24, ]),
                      ('_FICA_trt', [0.153,]),
                      ('_SS_percentage1', [0.5,]),
                      ('_SS_percentage2', [0.85,]),
                      ('_II_prt', [0.02,]),
                      ('_ID_Medical_frt', [0.075,]),
                      ('_ID_Casualty_frt', [0.1,]),
                      ('_ID_Miscellaneous_frt', [0.02,]),
                      ('_ID_Charity_crt_Cash', [0.5,]),
                      ('_ID_Charity_crt_Asset', [0.3,]),
                      ('_ID_prt', [0.03,]),
                      ('_ID_crt', [0.8,]),
                      ('_AMED_trt', [0.038,]),
                      ('_AMT_prt', [0.025,]),
                      ('_AMT_trt1', [0.26,]),
                      ('_AMT_trt2', [0.02,]),
                      ('_CTC_prt', [0.05,]),
                      ('_ACTC_ChildNum', [4,])]
        # INITIALIZE
        [setattr(self, name, expand_array(np.array(val),
             inflation_rate=inflation_rate, num_years=budget_years))
             for name, val in self._vals]

        self.set_year(start_year)

    @property
    def current_year(self):
        return self._current_year

    @property
    def start_year(self):
        return self._start_year

    def increment_year(self):
        self._current_year += 1
        self.set_year(self._current_year)

    def set_year(self, yr):
        for name, vals in self._vals:
            arr = getattr(self, name)
            setattr(self, name[1:], arr[yr-self._start_year])
