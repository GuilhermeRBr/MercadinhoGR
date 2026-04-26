import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="text-center">
        <h1 className="text-6xl font-bold text-gray-800 mb-4">
          Mercadinho GR
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Sistema de Gerenciamento
        </p>
        <Link
          href="/login"
          className="inline-block px-8 py-4 bg-blue-600 text-white rounded-lg shadow-lg hover:bg-blue-700 transition-colors font-medium"
        >
          Fazer Login
        </Link>
        <div className="mt-8 text-sm text-gray-500">
          STEP 3 - Autenticação implementada ✓
        </div>
      </div>
    </div>
  );
}
