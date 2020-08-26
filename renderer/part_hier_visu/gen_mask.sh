indir=$1
rm -rf $1/parts_render $1/*.html
python render_masks.py $1