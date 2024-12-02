{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "5570eab9-8faa-420c-a5a7-c663a21011ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "936063\n",
      "23150395\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "f = open('AOC_1.txt', 'r')\n",
    "content = f.read()\n",
    "number = content.split()\n",
    "list1 = []\n",
    "list2 = []\n",
    "for index, item in enumerate(number):\n",
    "    if index%2 == 0:\n",
    "        list1.append(int(item))\n",
    "    else:\n",
    "        list2.append(int(item))\n",
    "\n",
    "list1.sort()\n",
    "list2.sort()\n",
    "x = 0\n",
    "y = 0\n",
    "\n",
    "for index, item in enumerate(list1):\n",
    "    x += abs(list1[index]-list2[index])\n",
    "\n",
    "print(x)\n",
    "    \n",
    "for index, item in enumerate(list1):\n",
    "    y+= list1[index]* list2.count(list1[index])\n",
    "\n",
    "print(y)\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9c12600-901b-4e24-a968-996e629826c0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
