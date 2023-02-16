# from progress.bar import Bar
# import time
#
# br = Bar('Processing', max=20)
# for i in range(20):
# #    time.sleep(1)
#     print(i)
#     br.next()
# br.finish()
import time
import progressbar


for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)