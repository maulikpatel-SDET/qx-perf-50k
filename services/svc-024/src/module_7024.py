"""Service module 7024: business logic, no crypto."""


def calculate_total_7024(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7024():
    return 'module 7024 handles orders and invoices'
