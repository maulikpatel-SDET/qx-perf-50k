"""Service module 48082: business logic, no crypto."""


def calculate_total_48082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48082():
    return 'module 48082 handles orders and invoices'
