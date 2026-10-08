"""Service module 14477: business logic, no crypto."""


def calculate_total_14477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14477():
    return 'module 14477 handles orders and invoices'
