"""Service module 19154: business logic, no crypto."""


def calculate_total_19154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19154():
    return 'module 19154 handles orders and invoices'
