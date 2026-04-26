import { useMutation, useQueryClient } from "@tanstack/react-query";
import { paymentService } from "@/services/paymentService";
import { CreatePaymentDTO } from "@/types/Payment";
import { saleKeys } from "./useSales";

// Hook para criar pagamento
export function useCreatePayment() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: CreatePaymentDTO) => paymentService.create(data),
    onSuccess: () => {
      // Invalidar cache de vendas
      queryClient.invalidateQueries({ queryKey: saleKeys.lists() });
    },
  });
}
