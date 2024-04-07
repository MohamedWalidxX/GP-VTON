from torch import FloatTensor
from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        # for displays
        self.parser.add_argument(
            '--launcher', choices=['none', 'pytorch'], default='pytorch', help='job launcher')
        self.parser.add_argument('--local_rank', type=int, default=0)

        self.parser.add_argument('--write_loss_frep', type=int, default=100,
                                 help='frequency of showing training results on screen')
        self.parser.add_argument('--display_freq', type=int, default=100,
                                 help='frequency of showing training results on screen')
        self.parser.add_argument('--print_freq', type=int, default=100,
                                 help='frequency of showing training results on console')
        self.parser.add_argument('--save_latest_freq', type=int,
                                 default=1000, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=3,
                                 help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--no_html', action='store_true',
                                 help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        self.parser.add_argument('--debug', action='store_true',
                                 help='only do one epoch and displays at each iteration')

        # for training
        self.parser.add_argument('--continue_train', action='store_true',
                                 help='continue training: load the latest model')
        self.parser.add_argument('--load_pretrain', type=str, default='',
                                 help='load the pretrained model from the specified location')
        self.parser.add_argument('--which_epoch', type=str, default='latest',
                                 help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument(
            '--phase', type=str, default='train', help='train, val, test, etc')
        self.parser.add_argument(
            '--niter', type=int, default=70, help='# of iter at starting learning rate')
        self.parser.add_argument('--niter_decay', type=int, default=50,
                                 help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument(
            '--beta1', type=float, default=0.5, help='momentum term of adam')
        self.parser.add_argument(
            '--lr', type=float, default=1.8405570578796376e-05, help='initial learning rate for adam')
        self.parser.add_argument(
            '--lr_D', type=float, default=0.000020, help='initial learning rate for adam')
        self.parser.add_argument('--pretrain_checkpoint_D', type=str, default='/kaggle/input/3-epochs/flow/PBAFN_D_epoch_118.pth',
                                 help='load the pretrained model from the specified location')
        self.parser.add_argument('--PFAFN_warp_checkpoint', type=str,
                                 help='load the pretrained model from the specified location')
        self.parser.add_argument('--PFAFN_gen_checkpoint', type=str,
                                 help='load the pretrained model from the specified location')
        self.parser.add_argument('--PBAFN_warp_checkpoint', type=str, default= '/kaggle/input/3-epochs/flow/PBAFN_warp_epoch_118.pth', 
                                 help='load the pretrained model from the specified location')
        self.parser.add_argument('--PBAFN_gen_checkpoint', type=str,
                                 help='load the pretrained model from the specified location')

        self.parser.add_argument('--CPM_checkpoint', type=str)
        self.parser.add_argument('--CPM_D_checkpoint', type=str)

        self.parser.add_argument('--write_loss_frep_eval', type=int, default=100,
                                 help='frequency of showing training results on screen')
        self.parser.add_argument('--display_freq_eval', type=int, default=100,
                                 help='frequency of showing training results on screen')

        self.parser.add_argument('--add_mask_tvloss', action='store_true',
                                 help='if specified, use employ tv loss for the predicted composited mask')

        # for discriminators
        self.parser.add_argument(
            '--num_D', type=int, default=2, help='number of discriminators to use')
        self.parser.add_argument(
            '--n_layers_D', type=int, default=3, help='only used if which_model_netD==n_layers')
        self.parser.add_argument(
            '--ndf', type=int, default=64, help='# of discrim filters in first conv layer')
        self.parser.add_argument(
            '--lambda_feat', type=float, default=10.0, help='weight for feature matching loss')
        self.parser.add_argument('--no_ganFeat_loss', action='store_true',
                                 help='if specified, do *not* use discriminator feature matching loss')
        self.parser.add_argument('--no_vgg_loss', action='store_true',
                                 help='if specified, do *not* use VGG feature matching loss')
        self.parser.add_argument('--no_lsgan', action='store_true',
                                 help='do *not* use least square GAN, if false, use vanilla GAN')
        self.parser.add_argument('--pool_size', type=int, default=0,
                                 help='the size of image buffer that stores previously generated images')

        self.parser.add_argument('--debug_test', action='store_true')
        self.parser.add_argument(
            '--image_test_pairs_txt', type=str, default='')
        self.parser.add_argument(
            '--image_pairs_txt_eval', type=str, default='')
        self.parser.add_argument('--use_preserve_mask_refine', action='store_true',
                                 help='if specified, use preserve mask to refine to the warp clothes')

        self.parser.add_argument('--repeat_num', type=int, default=6)
        self.parser.add_argument('--loss_ce', type=float, default=1)
        self.parser.add_argument('--loss_gan', type=float, default=1)

        self.parser.add_argument('--debug_train', action='store_true')
        self.parser.add_argument('--test_flip', action='store_true')

        self.parser.add_argument(
            '--first_order_smooth_weight', type=float, default=0.01)
        self.parser.add_argument(
            '--squaretv_weight', type=float, default=1)

        self.parser.add_argument('--mask_epoch', type=int, default=70)
        self.parser.add_argument('--no_dynamic_mask', action='store_true')

        self.parser.add_argument('--resolution', type=int, default=512)
        self.parser.add_argument('--dataset', type=str, default='vitonhd')

        self.isTrain = True
