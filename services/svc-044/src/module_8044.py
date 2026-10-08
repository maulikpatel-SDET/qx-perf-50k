"""Service module 8044: business logic, no crypto."""


def calculate_total_8044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8044():
    return 'module 8044 handles orders and invoices'
