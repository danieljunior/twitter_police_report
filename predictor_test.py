from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("results/model.tar.gz","srl")
result = predictor.predict(
  sentence="Jovem e vitima de assalto em Niteroi."
)
print(result)
