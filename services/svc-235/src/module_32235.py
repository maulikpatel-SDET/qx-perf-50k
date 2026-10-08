"""Service module 32235: business logic, no crypto."""


def calculate_total_32235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32235():
    return 'module 32235 handles orders and invoices'
