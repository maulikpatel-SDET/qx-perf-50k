"""Service module 17044: business logic, no crypto."""


def calculate_total_17044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17044():
    return 'module 17044 handles orders and invoices'
