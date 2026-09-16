class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        resultado = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                indice_antigo = stack.pop()
                resultado[indice_antigo] = i - indice_antigo
            stack.append(i)


        return resultado
            