## CS32 Chapter 8 (Act I, Scene III) Programming Assignment

In this pset, you'll have the opportunity to act a bit like a data scientist, using the tools of a data scientist. Our Friday section focused on data cleaning, and this pset will focus on **data exploration**. It builds off our knowledge of digital images and has fun with the wacky world of Where's Waldo.

**The IDE for the pset.** Both parts of this assignment will have you working in [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb), which is an online environment meant to look like a scientist's notebook. You've had some practice with this environment through our class notes. A popular alternative to Google Colab is [the Jupyter Notebook](https://jupyter.org/). Both are sophisticated web applications in which you stitch together narrative text with Python code, images, and other data visualizations. Both platforms manipulate files in IPYNB format. If you're familiar with Jupyter Notebooks, you may use that IDE instead of Google Colab.

**Big picture.** The code that you'll write:

*   In the first part will teach you how to hide an image of Wenda in an image of Harvard Yard and, of course, later recover that Wenda image. In doing this work, you'll practice using bitwise operators and get more comfortable creating code that does limited traversals of the pixels in one or more images.
*   In the second part will have you practice different traversals over the pixels of an image (in particular, a Harvard image in which we've hidden Wenda and one or more Odlaw characters). The looping structures you'll build and the thinking you'll do about how to use Python exceptions to cleanly unwind a computation (i.e., to stop one analysis and start another) will be useful in the exploration of any kind of data set.

**Ready to get started?**

1.   Please download `pset4-part1.ipynb` from the Modules page of our course Canvas site and upload it into a Google Colab session. Then complete the work described in it. When you've completed that notebook, move on to the second part below.
2.   After completing the first notebook, continue on with `pset4-part2.ipynb`. Download it from the Modules page and upload it into Colab. Follow the directions within it.

For each notebook, don't forget to execute each code block as you come across it!

**Submission.** When you finish, you will submit three files:

1.   The **two ipynb notebooks** in which you worked. In Google Colab, click the *File* menu item, select *Download*, and then *Download ipynb*. This will download a copy of your completed notebook to your computer. Do this for each notebook, and then submit both.
2.   **A PDF file containing your name and a link to a video explanation** in which you take the teaching staff through the code you've written in each notebook. As always, you should explain what your code does, and then a demonstration it in action. Please make sure that we have permissions to view your video.

As is true for all submissions here in Act I, your code doesn't have to work perfectly to get full credit. Review the rules from pset1 if you've forgotten exactly what we expect from you.

Congratulations on everything you've learned in Act I!
