{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "8\n",
      "10\n",
      "13\n",
      "15\n",
      "19\n",
      "20\n",
      "23\n",
      "25\n",
      "[7, 8, 10, 13, 15, 19, 20, 23, 25]\n",
      "7\n",
      "8\n",
      "10\n",
      "13\n",
      "19\n",
      "20\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "nums = list([int(input()) for i in range(9)])\n",
    "tot = sum(nums)\n",
    "\n",
    "for i in range(8):\n",
    "    for j in range(i+1,9):\n",
    "        if(nums[i]+nums[j] == tot - 100):\n",
    "            nums.pop(j)\n",
    "            nums.pop(i)\n",
    "            break;\n",
    "    if(sum(nums)==100):\n",
    "        break;\n",
    "        \n",
    "for i in nums:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "7 8 10 13 15 19 20 23 25"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
