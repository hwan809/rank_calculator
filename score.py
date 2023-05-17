def rank(weights, scores):
    rank = 0

    for i in range(len(scores)):
        rank += weights[i] * scores[i]

    return rank / sum(weights)

if __name__ == '__main__':
    weights = list(map(int, input('단위수를 공백으로 구분하여 입력: ').split()))
    scores = list(map(float, input('등수를 공백으로 구분하여 입력: ').split()))

    print(f'{rank(weights, scores)} 등')