"""Service module 46054: business logic, no crypto."""


def calculate_total_46054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46054():
    return 'module 46054 handles orders and invoices'
