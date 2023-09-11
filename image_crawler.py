from os.path import exists
from os import mkdir, listdir
from string import punctuation


def download_images(sub_material, target_count, bin):
    # clean up submaterial name
    sub_material = sub_material.replace('/', '').replace('\\', '')
    
    bfolder = f'geelong-recycling-instructions/images/{bin}'
    folder = f'geelong-recycling-instructions/images/{bin}/{sub_material}'

    # checks if the folder for submaterial exists, 
    if not exists(bfolder):
        mkdir(bfolder)

    # checks if the folder for submaterial exists, 
    if not exists(folder):
        mkdir(folder)
    else:
        # download already done, so just move on
        return folder, len(list(listdir(folder)))

    # create the crawler object
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={
            'root_dir': folder
        },
        log_level=50,  # setting it to critical only
    )

    # run the crawler
    google_crawler.crawl(keyword=sub_material, max_size=(1024, 1024), max_num=int(target_count))
    
    return folder, len(list(listdir(folder)))


def call_download(df, bin):
    download_summary = {
        'sub_material': [],
        'target_count': [],
        'download_count': [],
        'target_met': [],
        'download_path': [],
    }
    for idx, row in df.iterrows():
        sub_material = row.sub_material
        target_count = row.image_pull_count
        folder, download_count = download_images(sub_material, target_count, bin)
        download_summary['sub_material'].append(sub_material)
        download_summary['target_count'].append(target_count)
        download_summary['download_count'].append(download_count)
        download_summary['target_met'].append(target_count==download_count)
        download_summary['download_path'].append(folder)
    
    return DataFrame(download_summary)


dropoff_download_summary = call_download(dropoff_proportions, 'dropoff')
red_download_summary = call_download(red_proportions, 'red')
yellow_download_summary = call_download(yellow_proportions, 'yellow')
green_download_summary = call_download(green_proportions, 'green')