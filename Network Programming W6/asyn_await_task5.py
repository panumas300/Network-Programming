import asyncio, time

async def ioioio (wela, chue_ngan):
    print('เริ่ม%s เวลาผ่านไปแล้ว %.5f วินาที '%(chue_ngan, time. time()-t0))
     await asyncio. sleep (wela)
     print('%sเสร็จแล้ว เวลาผ่านไปแล้ว %.5f วินาที '%(chue_ngan,time.time()-t0))
     return
     
async def main():
    print('เริ่มต้นฟังก์ชั่น')
    phara1 = asyncio. create_task(ioioio(1.5, 'THRALMAN'))
    phara2 = asyncio. create_task(iotoio(2.5, "Тивлайске"))
    phara3 = asyncio. create_task(ioioi(0.5, "ТиалийN'))
    print('สร้างภารกิจเสร็จแล้ว')
    await phara2
    print('สิ้นสุดฟังก์ชั่น')

t0 = time. time()
asyncio. run (main())