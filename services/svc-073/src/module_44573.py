"""Service module 44573: business logic, no crypto."""


def calculate_total_44573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44573():
    return 'module 44573 handles orders and invoices'
