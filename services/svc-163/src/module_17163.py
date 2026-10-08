"""Service module 17163: business logic, no crypto."""


def calculate_total_17163(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17163():
    return 'module 17163 handles orders and invoices'
