"""Service module 47044: business logic, no crypto."""


def calculate_total_47044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47044():
    return 'module 47044 handles orders and invoices'
