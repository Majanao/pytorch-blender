import bpy
import numpy as np
from blendtorch import btb

import sys
sys.path.append('C:/dev/supershape')
import supershape as sshape

def main():

    #btargs, remainder = btb.parse_blendtorch_args()

    SHAPE=(100,100)
    x,y,z = sshape.supercoords(sshape.FLOWER, shape=SHAPE)
    obj = sshape.make_bpy_mesh(x, y, z)

    def pre_frame():
        # Randomize cube rotation
        params = np.array(sshape.FLOWER)
        params[0] += np.random.normal(scale=2.0)
        x,y,z = sshape.supercoords(params, shape=SHAPE)
        sshape.update_bpy_mesh(x,y,z,obj)
        
    def post_frame(off):
        off.render()
        # Called every after Blender finished processing a frame.
        # Will be sent to one of the remote dataset listener connected.
        # pub.publish(
        #     image=off.render(), 
        #     xy=cam.object_to_pixel(cube), 
        #     frameid=anim.frameid
        # )
        pass

    # Data source
    #pub = btb.DataPublisher(btargs.btsockets['DATA'], btargs.btid)

    # Setup default image rendering
    cam = btb.Camera()
    off = btb.OffScreenRenderer(camera=cam, mode='rgb')
    off.set_render_style(shading='SOLID', overlays=False)

    # Setup the animation and run endlessly
    anim = btb.AnimationController()
    anim.pre_frame.add(pre_frame)
    anim.post_frame.add(post_frame, off)
    anim.play(frame_range=(0,100), num_episodes=-1)

    
main()

