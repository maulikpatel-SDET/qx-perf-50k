"""Service module 6221: business logic, no crypto."""


def calculate_total_6221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6221():
    return 'module 6221 handles orders and invoices'
