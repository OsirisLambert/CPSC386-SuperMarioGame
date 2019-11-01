import Castle
import QuestionBrick
import NormalBrick
import WarpPipe
import Flag
import GroundBrick
import unmoveable_item
import MoveStep
import goomba
import Koopa

class world1_1():
    def __init__(self, SuperMario):

        SuperMario.goombas.add(goomba.Goomba(1080, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(2000, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(2450, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(2520, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(3766, 176, 1))
        SuperMario.goombas.add(goomba.Goomba(3826, 176, 1))
        SuperMario.goombas.add(goomba.Goomba(4200, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(4260, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(4320, 560, 1))
        SuperMario.goombas.add(goomba.Goomba(4390, 560, 1))

        SuperMario.koopas.add(Koopa.Koopa(600, 560, 1))

        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(771, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(1000, 408, 1))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(1080, 408, 1))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(1040, 216, 1))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(3736, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(3736, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(4576, 216))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(4976, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(5056, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(5056, 216))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(5136, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(5736, 216))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(5776, 216))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(7116, 408))

        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(960, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1040, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1120, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3696, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3776, 408))
        for index in range(4016, 4337, 40):
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 216))
        for index in range(4656, 4577, 40):
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 216))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(4576, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(4776, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(4816, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5336, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5416, 216))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5456, 216))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5496, 216))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5736, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5776, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5816, 216))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(7036, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(7076, 408))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(7156, 408))

        SuperMario.normalPipes.add(WarpPipe.NormalPipe(1347, 507, 80, 93))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(1824, 459, 80, 141))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(2208, 408, 80, 192))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(2736, 408, 80, 192))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(6856, 507, 80, 93))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(7792, 507, 80, 93))

        for index in range(5896, 6017, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 560))
        for index in range(5936, 6017, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 520))
        for index in range(5976, 6017, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 480))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6016, 440))
        for index in range(6136, 6257, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 560))
        for index in range(6136, 6217, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 520))
        for index in range(6136, 6177, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 480))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6136, 440))
        for index in range(6336, 6497, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 560))
        for index in range(6376, 6497, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 520))
        for index in range(6416, 6497, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 480))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6456, 440))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6496, 440))
        for index in range(6616, 6737, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 560))
        for index in range(6616, 6697, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 520))
        for index in range(6616, 6657, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 480))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6616, 440))

        for index in range(7872, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 560))
        for index in range(7912, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 520))
        for index in range(7952, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 480))
        for index in range(7992, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 440))
        for index in range(8032, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 400))
        for index in range(8072, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 360))
        for index in range(8112, 8193, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(index, 320))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(8152, 280))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(8192, 280))
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(8700, 560))

        for index in range(0, 3363, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600))
        for index in range(3480, 4201, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600))
        for index in range(4377, 6498, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600))
        SuperMario.groundBlocks.add(GroundBrick.GroundBrick(6500, 600))
        for index in range(6615, 30519, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600))

        SuperMario.flags.add(Flag.Flagpole(8720, 200))
        SuperMario.flags.add(Flag.Flag(8680, 210))

        SuperMario.instruction_board.add(unmoveable_item.Instruction_board(50,100))
        SuperMario.castles.add(Castle.Castle(8852, 400))

        for index in range(10, 10000,900):
            SuperMario.clouds.add(unmoveable_item.Cloud(index, 200, 'small'))
            SuperMario.brushes.add(unmoveable_item.Brush(index, 555, 'small'))
        for index in range(1200, 10000, 2060):
            SuperMario.clouds.add(unmoveable_item.Cloud(index, 200, 'large'))
            SuperMario.mountains.add(unmoveable_item.Mountain(index, 550, 'small'))
        for index in range(390, 10000, 1200):
            SuperMario.mountains.add(unmoveable_item.Mountain(index, 500, 'large'))
        for index in range(800, 10000, 1200):
            SuperMario.brushes.add(unmoveable_item.Brush(index, 555, 'large'))

        SuperMario.unmove_items.add(SuperMario.brushes, SuperMario.clouds, SuperMario.mountains, SuperMario.instruction_board)
        SuperMario.enemies.add(SuperMario.goombas, SuperMario.koopas)
        SuperMario.blocks.add(SuperMario.QuestionBlocks, SuperMario.flags, SuperMario.castles, SuperMario.groundBlocks,
                              SuperMario.groundUpBlocks, SuperMario.normalPipes, SuperMario.normalBlocks)


class world1_2():
    def __init__(self, SuperMario):
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(480, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(520, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(560, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(600, 408))
        SuperMario.QuestionBlocks.add(QuestionBrick.QuestionBrick(640, 408))


        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1299, 400, '1-2'))
        for index in range(360, 441, 40):
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1872, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1952, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2072, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2152, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2496, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2536, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2496, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2816, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2856, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3096, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3136, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3296, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3496, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3536, index, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1912, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(1992, 360, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2032, 360, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2112, 440, '1-2'))
        for index in range(440, 521, 40):
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2576, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2616, index, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2736, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2776, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(2976, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3376, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3656, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3696, 440, '1-2'))
        SuperMario.normalBlocks.add(NormalBrick.NormalBrick(3736, 440, '1-2'))  # 3736gap
        for index in range(480, 561, 40):
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5670, index, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(5710, index, '1-2'))  # 5710 gap
        for index in range(3976, 4177, 40):  # 3936 gap
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 410, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 370, '1-2'))
        for index in range(6790, 6991, 40):  # 3936 gap
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 410, '1-2'))
        for index in range(7310, 7671, 40):  # 3936 gap
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 560, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 520, '1-2'))
            SuperMario.normalBlocks.add(NormalBrick.NormalBrick(index, 480, '1-2'))



        SuperMario.normalPipes.add(WarpPipe.NormalPipe(4950, 460, 80, 140))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(5190, 410, 80, 190))
        SuperMario.normalPipes.add(WarpPipe.NormalPipe(5430, 540, 80, 60))  # 5550 gap
        # SuperMario.normalPipes.add(QuestionBrick.NormalPipe(5430, 540, 80, 60))



        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(819, 560, '1-2'))
        for index in range(520, 561, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(899, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(1459, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6430, index, '1-2'))
        for index in range(480, 561, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(979, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(1219, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(1379, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6470, index, '1-2'))
        for index in range(440, 561, 40):
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(1059, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(1139, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6510, index, '1-2'))
            SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6550, index, '1-2'))  # 6550 gap
        SuperMario.groundUpBlocks.add(GroundBrick.GroundUpBrick(6390, index, '1-2'))  # 5670 gap


        for index in range(0, 3736, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600, '1-2'))
        SuperMario.groundBlocks.add(GroundBrick.GroundBrick(3736, 600, '1-2'))
        for index in range(3856, 5551, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600, '1-2'))
        SuperMario.groundBlocks.add(GroundBrick.GroundBrick(5550, 600, '1-2'))
        for index in range(5670, 5711, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600, '1-2'))
        for index in range(5830, 6551, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600, '1-2'))
        for index in range(6790, 7071, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600, '1-2'))
        for index in range(7310, 30000, 40):
            SuperMario.groundBlocks.add(GroundBrick.GroundBrick(index, 600, '1-2'))


        SuperMario.move_steps.add(MoveStep.Move_step(6640, 400))
        SuperMario.move_steps.add(MoveStep.Move_step(6640, 600))

        SuperMario.move_steps.add(MoveStep.Move_step(7160, 350))
        SuperMario.move_steps.add(MoveStep.Move_step(7160, 550))

        SuperMario.long_pipes.add(WarpPipe.Long_pipe(7510, 160))

        SuperMario.blocks.add(SuperMario.move_steps)
        SuperMario.blocks.add(SuperMario.normalBlocks)
        SuperMario.blocks.add(SuperMario.long_pipes)
        SuperMario.blocks.add(SuperMario.groundBlocks)
        SuperMario.blocks.add(SuperMario.groundUpBlocks)
        SuperMario.blocks.add(SuperMario.normalPipes)
        SuperMario.blocks.add(SuperMario.QuestionBlocks)