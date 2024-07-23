This directory contains everything needed for
**Chapter 8 (What is My Problem?)** in
[*Computational Thinking and Problem Solving (CTPS)*](https://profsmith89.github.io/ctps/ctps.html)
by Michael D. Smith.

`ale02.py`: The starter code for ALE #2.  Its code contents are the same as
ALE #5 from Chapter 6.

`images/photobomb[1-3].jpg`: Three images of Waldo moving through Harvard Yard.
We'd like the picture of the Yard with Waldo removed.  We created this sequence
of pictures by copying a single picture of Harvard Yard and then inserting Waldo
in three different locations.

`images/photobomb-mode.jpg`: The result of a version of the `ale01` script
that uses `statistics.mode` instead of `statistics.median`.  It looks good,
right?

`images/duck[1-3]*.jpg`: Three images of a common background and an object (the
CS50 ddb duck) that we'd like to eliminated.  This is a real sequence of three
pictures, and as such, even the pixels where the duck isn't even placed are
subtly different from picture to picture. The images come in both black-and-white
and color.

`images/duck-mode.jpg`: The result of a version of the `ale01` script that
uses `statistics.mode` instead of `statistics.median`.  It does NOT look good!
Your answer to ALE #1, step 7 will explain why.

`images/apsu[1-6].jpg`: Seven actual images of a common background and a person
who we'd like to remove from the picture.  The unintended subject overlaps
himself in any three of these pictures, and thus we need more than three
pictures to completely remove him.  Thanks again to John Nicholson, from whose
original assignment we got these pictures.

`zero.py`: Script illustrating the clearing of the lowest 4 bits in each channel
of the pixels in an image.

`images/harvard.png`: The original image of Harvard Yard without Waldo
photobombing it. I didn't take this picture.

`images/garden*.png`: The original image of the Boston Public Garden without
Waldo photobombing it. I took this picture. This image comes in both
black-and-white and color.

`xverse.py`: A script that uses simple modifications to images to illustrate
different traversals of 2-dimensional data.
