"""Service module 4266: business logic, no crypto."""


def calculate_total_4266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4266():
    return 'module 4266 handles orders and invoices'
