{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQDGAtNUNKVFfG7BIh0MKt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/davekgw/Kompro-1/blob/main/Gaji_karyawan.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OLwzGiDef-kz",
        "outputId": "57c7d431-acb0-4bba-9d52-3c975a0ad846"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan golongan anda (1-4): 1\n",
            "Masukkan berapa lama jam kerja anda: 45\n",
            "\n",
            "Gajimu = Rp.135150\n"
          ]
        }
      ],
      "source": [
        "gol1 = 3000\n",
        "gol2 = 3500\n",
        "gol3 = 4000\n",
        "gol4 = 5000\n",
        "while True:\n",
        "  gol = int(input(\"Masukkan golongan anda (1-4): \"))\n",
        "  if (gol == 1 or gol == 2 or gol == 3 or gol == 4):\n",
        "    break\n",
        "  else:\n",
        "    print(\"Masukan golongan yang benar!!\")\n",
        "\n",
        "jam = int(input(\"Masukkan berapa lama jam kerja anda: \"))\n",
        "if (gol == 1):\n",
        "  gaji = gol1 * jam\n",
        "  if (jam > 40):\n",
        "    gaji = 40 * gol1 + (jam - 40) * gol1 * 1.01\n",
        "elif (gol == 2):\n",
        "  gaji = gol2 * jam\n",
        "  if (jam > 40):\n",
        "    gaji = 40 * gol2 + (jam - 40) * gol2 * 1.01\n",
        "elif (gol == 3):\n",
        "  gaji = gol3 * jam\n",
        "  if (jam > 40):\n",
        "    gaji = 40 * gol3 + (jam - 40) * gol3 * 1.01\n",
        "elif (gol == 4):\n",
        "  gaji = gol4 * jam\n",
        "  if (jam > 40):\n",
        "    gaji = 40 * gol4 + (jam - 40) * gol4 * 1.01\n",
        "\n",
        "\n",
        "print(f\"\\nGajimu = Rp.{int(gaji)}\")\n",
        "\n"
      ]
    }
  ]
}