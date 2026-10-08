"""Service module 47014: business logic, no crypto."""


def calculate_total_47014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47014():
    return 'module 47014 handles orders and invoices'
