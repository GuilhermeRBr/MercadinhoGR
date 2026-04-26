import Link from "next/link";
import { LogIn, UserPlus, ShoppingBag } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      <div className="text-center max-w-2xl px-6">
        {/* Logo/Ícone */}
        <div className="inline-flex items-center justify-center w-24 h-24 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-3xl shadow-2xl mb-8">
          <ShoppingBag className="w-12 h-12 text-white" />
        </div>

        {/* Título */}
        <h1 className="text-6xl font-bold text-gray-800 mb-4">
          Mercadinho GR
        </h1>
        <p className="text-xl text-gray-600 mb-12">
          Sistema Completo de Gerenciamento
        </p>

        {/* Botões */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <Link
            href="/login"
            className="inline-flex items-center gap-3 px-8 py-4 bg-blue-600 text-white rounded-xl shadow-lg hover:bg-blue-700 hover:shadow-xl transition-all font-medium text-lg w-full sm:w-auto justify-center"
          >
            <LogIn className="w-5 h-5" />
            Fazer Login
          </Link>
          <Link
            href="/register"
            className="inline-flex items-center gap-3 px-8 py-4 bg-white text-blue-600 border-2 border-blue-600 rounded-xl shadow-lg hover:bg-blue-50 hover:shadow-xl transition-all font-medium text-lg w-full sm:w-auto justify-center"
          >
            <UserPlus className="w-5 h-5" />
            Criar Conta
          </Link>
        </div>

        {/* Features */}
        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
          <div className="bg-white p-6 rounded-xl shadow-md">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
              <ShoppingBag className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">PDV Completo</h3>
            <p className="text-sm text-gray-600">
              Sistema de caixa rápido e intuitivo para vendas
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-md">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
              <LogIn className="w-6 h-6 text-green-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">Gestão Total</h3>
            <p className="text-sm text-gray-600">
              Controle de produtos, vendas e usuários
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-md">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
              <UserPlus className="w-6 h-6 text-purple-600" />
            </div>
            <h3 className="font-semibold text-gray-800 mb-2">Dashboard</h3>
            <p className="text-sm text-gray-600">
              Estatísticas e relatórios em tempo real
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-12 text-sm text-gray-500">
          Sistema Completo v1.0.0 • Todos os módulos implementados ✓
        </div>
      </div>
    </div>
  );
}
