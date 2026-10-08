"""Service module 27235: business logic, no crypto."""


def calculate_total_27235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27235():
    return 'module 27235 handles orders and invoices'
