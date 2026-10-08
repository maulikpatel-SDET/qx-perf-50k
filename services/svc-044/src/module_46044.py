"""Service module 46044: business logic, no crypto."""


def calculate_total_46044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46044():
    return 'module 46044 handles orders and invoices'
