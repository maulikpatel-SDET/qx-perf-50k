"""Service module 44306: business logic, no crypto."""


def calculate_total_44306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44306():
    return 'module 44306 handles orders and invoices'
