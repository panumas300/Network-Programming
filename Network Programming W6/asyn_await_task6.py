import asyncio, time

async def ioioio (wela, chue_ngan):
    print('เริ่มต้น%s ผ่านไปแล้ว %.6f วินาที'%(chue_ngan, time. time ()-t0) )
    await asyncio. S leep (wela)
    print('%sเสร็จสิ้น ผ่านไปแล้ว %.6f วินาที'%(chue_ngan, time. time ()-t0) )

async def main():
    cococoru = [ioioio(1.5,'โหลดเพลง'),ioioio(2.5,'โหลดอนิเมะ'),ioioio(0.5,'โหลดหนัง'),ioioio(2,'โหลดเกม')]
    await asyncio.wait(cococoru)

to = time.time()
asyncio.run(main())