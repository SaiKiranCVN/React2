// import {useEffect, useState} from 'react';




const data = {
  exchanges: [
    {
      name: "ann",
      index: 123,
      change: 0.52,
    },
    {
      name: "sean",
      index: 123,
      change: 0.52,
    },
    {
      name: "Eref",
      index: 123,
      change: 0.52,
    },
    {
      name: "Hang",
      index: 123,
      change: 0.52,
    },
  ],
  stocks: [
    {
      name: "Apple",
      ticker: "AAPL",
      bid: 128.5,
      ask: 129.0,
      sector: "Technology",
      change: 1.54,
      dividends: {
        2021:35,
        2020: 20,
        2019: 19,
        2018: 18,
        2017: 15,
        2016: 13,
        2015: 10,
        2014: 12,
        2013: 15,
        2012: 10,
        2011: 15,
        2010: 12,
        2009: 3,
        2008: 5,
        2007: 12,
        2006: 15,
        2005: 5,
        2004: 3,
      },
      homepage: "https://apple.com",
      investorpage: "https://apple.com",
      pe: 15,
      research: [
        {
          title: "First research",
          description:
            "This is the description. It is usually a lot longer than the title and contains information about the research that has been done",
          link: "https://apple.com",
          author: { name: "Ann", authorId: "author123" },
          id: 1,
        },
      ],
    },
    {
      name: "Tesla",
      ticker: "TSLA",
      bid: 128.5,
      ask: 129.0,
      sector: "Transport",
      change: 1.54,
      dividends: {
        2021:24,
        2020: 23,
        2019: 5,
        2018: 18,
        2017: 15,
        2016: 13,
        2015: 10,
      },
      homepage: "https://tesla.com",
      investorpage: "https://tesla.com",
      pe: 15,
      research: [
        {
          title: "First research",
          description:
            "This is the description. It is usually a lot longer than the title and contains information about the research that has been done",
          link: "https://tesla.com",
          author: { name: "Ann", authorId: "author123" },
          id: 1,
        },
        {
          title: "Second research",
          description:
            "This is the description. It is usually a lot longer than the title and contains information about the research that has been done",
          link: "https://google.com",
          author: { name: "Ann", authorId: "author123" },
          id: 2,
        },
      ],
    },
    {
      name: "Amazon",
      ticker: "AMZN",
      bid: 128.5,
      ask: 129.0,
      sector: "Sales",
      change: 1.54,
      dividends: {
        2021:0.19,
        2020: 13,
        2019: 15,
        2018: 18,
        2017: 15,
        2016: 13,
        2015: 10,
      },
      homepage: "https://amazon.com",
      investorpage: "https://amazon.com",
      pe: 15,
      research: [
        {
          title: "First research",
          description:
            "This is the description. It is usually a lot longer than the title and contains information about the research that has been done",
          link: "https://amazon.com",
          author: { name: "Ann", authorId: "author123" },
          id: 1,
        },
      ],
    },
    {
      name: "Microsoft",
      ticker: "MFST",
      bid: 128.5,
      ask: 129.0,
      sector: "Technology",
      change: 1.54,
      dividends: {
        2021:0.159,
        2020: 2,
        2019: 3,
        2018: 18,
        2017: 15,
        2016: 13,
        2015: 10,
      },
      homepage: "https://microsoft.com",
      investorpage: "https://microsoft.com",
      pe: 15,
      research: [
        {
          title: "First research",
          description:
            "This is the description. It is usually a lot longer than the title and contains information about the research that has been done",
          link: "https://google.com",
          author: { name: "Ann", authorId: "author123" },
          id: 1,
        },
      ],
    },
    {
      name: "Nvidia",
      ticker: "NVDA",
      bid: 128.5,
      ask: 129.0,
      sector: "Industry",
      change: 1.54,
      dividends: {
        2021:0.18,
        2020: 0.2,
        2019: 3,
        2018: 18,
        2017: 15,
        2016: 13,
        2015: 10,
      },
      homepage: "https://nvidia.com",
      investorpage: "https://nvidia.com",
      pe: 15,
      research: [
        {
          title: "Second research",
          description:
            "This is the description. It is usually a lot longer than the title and contains information about the research that has been done",
          link: "https://google.com",
          author: { name: "Ann", authorId: "author123" },
          id: 1,
        },
      ],
    },
  ],
};

export default data;
