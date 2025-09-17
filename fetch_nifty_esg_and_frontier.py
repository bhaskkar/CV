{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOErLdg+Ic4aJ91lNMbFsVl",
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
        "<a href=\"https://colab.research.google.com/github/bhaskkar/CV/blob/main/fetch_nifty_esg_and_frontier.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rBSaByAFrO_S",
        "outputId": "c9115cde-8331-4cb5-c082-0962bf4e66cb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (2.32.4)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.12/dist-packages (4.13.5)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.12/dist-packages (5.4.0)\n",
            "Requirement already satisfied: yfinance in /usr/local/lib/python3.12/dist-packages (0.2.65)\n",
            "Collecting pyportfolioopt\n",
            "  Downloading pyportfolioopt-1.5.6-py3-none-any.whl.metadata (22 kB)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.12/dist-packages (4.67.1)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (3.10.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests) (2025.8.3)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.12/dist-packages (from beautifulsoup4) (2.8)\n",
            "Requirement already satisfied: typing-extensions>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from beautifulsoup4) (4.15.0)\n",
            "Requirement already satisfied: multitasking>=0.0.7 in /usr/local/lib/python3.12/dist-packages (from yfinance) (0.0.12)\n",
            "Requirement already satisfied: platformdirs>=2.0.0 in /usr/local/lib/python3.12/dist-packages (from yfinance) (4.4.0)\n",
            "Requirement already satisfied: frozendict>=2.3.4 in /usr/local/lib/python3.12/dist-packages (from yfinance) (2.4.6)\n",
            "Requirement already satisfied: peewee>=3.16.2 in /usr/local/lib/python3.12/dist-packages (from yfinance) (3.18.2)\n",
            "Requirement already satisfied: curl_cffi>=0.7 in /usr/local/lib/python3.12/dist-packages (from yfinance) (0.13.0)\n",
            "Requirement already satisfied: protobuf>=3.19.0 in /usr/local/lib/python3.12/dist-packages (from yfinance) (5.29.5)\n",
            "Requirement already satisfied: websockets>=13.0 in /usr/local/lib/python3.12/dist-packages (from yfinance) (15.0.1)\n",
            "Requirement already satisfied: cvxpy>=1.1.19 in /usr/local/lib/python3.12/dist-packages (from pyportfolioopt) (1.6.7)\n",
            "Collecting ecos<3.0.0,>=2.0.14 (from pyportfolioopt)\n",
            "  Downloading ecos-2.0.14-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.0 kB)\n",
            "Requirement already satisfied: plotly<6.0.0,>=5.0.0 in /usr/local/lib/python3.12/dist-packages (from pyportfolioopt) (5.24.1)\n",
            "Requirement already satisfied: scipy>=1.3 in /usr/local/lib/python3.12/dist-packages (from pyportfolioopt) (1.16.1)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.59.2)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.4.9)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (25.0)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (11.3.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.2.3)\n",
            "Requirement already satisfied: cffi>=1.12.0 in /usr/local/lib/python3.12/dist-packages (from curl_cffi>=0.7->yfinance) (2.0.0)\n",
            "Requirement already satisfied: osqp>=0.6.2 in /usr/local/lib/python3.12/dist-packages (from cvxpy>=1.1.19->pyportfolioopt) (1.0.4)\n",
            "Requirement already satisfied: clarabel>=0.5.0 in /usr/local/lib/python3.12/dist-packages (from cvxpy>=1.1.19->pyportfolioopt) (0.11.1)\n",
            "Requirement already satisfied: scs>=3.2.4.post1 in /usr/local/lib/python3.12/dist-packages (from cvxpy>=1.1.19->pyportfolioopt) (3.2.8)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.12/dist-packages (from plotly<6.0.0,>=5.0.0->pyportfolioopt) (8.5.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.12/dist-packages (from cffi>=1.12.0->curl_cffi>=0.7->yfinance) (2.23)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from osqp>=0.6.2->cvxpy>=1.1.19->pyportfolioopt) (3.1.6)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from osqp>=0.6.2->cvxpy>=1.1.19->pyportfolioopt) (75.2.0)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.12/dist-packages (from osqp>=0.6.2->cvxpy>=1.1.19->pyportfolioopt) (1.5.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->osqp>=0.6.2->cvxpy>=1.1.19->pyportfolioopt) (3.0.2)\n",
            "Downloading pyportfolioopt-1.5.6-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading ecos-2.0.14-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (222 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m222.1/222.1 kB\u001b[0m \u001b[31m8.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: ecos, pyportfolioopt\n",
            "Successfully installed ecos-2.0.14 pyportfolioopt-1.5.6\n"
          ]
        }
      ],
      "source": [
        "pip install pandas numpy requests beautifulsoup4 lxml yfinance pyportfolioopt tqdm matplotlib\n"
      ]
    }
  ]
}