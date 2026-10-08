"""Service module 30044: business logic, no crypto."""


def calculate_total_30044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30044():
    return 'module 30044 handles orders and invoices'
