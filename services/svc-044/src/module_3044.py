"""Service module 3044: business logic, no crypto."""


def calculate_total_3044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3044():
    return 'module 3044 handles orders and invoices'
