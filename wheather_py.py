{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "wheather.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNaYcqxI8hPYSoTFDOidCv6",
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
        "<a href=\"https://colab.research.google.com/github/DilisDenny/ShapeAl_Bootcamp_BWD/blob/main/wheather_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zz4HyuocgHLE",
        "outputId": "c673a8e0-389b-4ccf-e9ca-e2ac6cedff46"
      },
      "source": [
        "import requests\n",
        "from datetime import datetime\n",
        "\n",
        "api_key = '3fc064e2113400eaf596a0b8328ae3b9'\n",
        "location = input(\"Enter the city name: \")\n",
        "\n",
        "complete_api_link = \"https://api.openweathermap.org/data/2.5/weather?q=\"+location+\"&appid=\"+api_key\n",
        "api_link = requests.get(complete_api_link)\n",
        "api_data = api_link.json()\n",
        "\n",
        "temp_city = ((api_data['main']['temp']) - 273.15)\n",
        "weather_desc = api_data['weather'][0]['description']\n",
        "hmdt = api_data['main']['humidity']\n",
        "wind_spd = api_data['wind']['speed']\n",
        "date_time = datetime.now().strftime(\"%d %b %Y | %I:%M:%S %p\")\n",
        "\n",
        "print (\"-------------------------------------------------------------\")\n",
        "print (\"Weather Stats for - {}  || {}\".format(location.upper(), date_time))\n",
        "print (\"-------------------------------------------------------------\")\n",
        "\n",
        "print (\"Current temperature is: {:.2f} deg C\".format(temp_city))\n",
        "print (\"Current weather desc  :\",weather_desc)\n",
        "print (\"Current Humidity      :\",hmdt, '%')\n",
        "print (\"Current wind speed    :\",wind_spd ,'kmph')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the city name: Thodupuzha\n",
            "-------------------------------------------------------------\n",
            "Weather Stats for - THODUPUZHA  || 23 Jun 2021 | 10:53:42 AM\n",
            "-------------------------------------------------------------\n",
            "Current temperature is: 28.83 deg C\n",
            "Current weather desc  : overcast clouds\n",
            "Current Humidity      : 77 %\n",
            "Current wind speed    : 2.25 kmph\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}